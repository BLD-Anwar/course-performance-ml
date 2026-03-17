# import pandas as pd

# def clean_data(df):
#     df = df.drop_duplicates()
#     df = df.dropna()
#     return df


# def create_features(df):
#     df["academic_score"] = (
#         df["assignment_avg"] * 0.3 +
#         df["quiz_avg"] * 0.3 +
#         df["midterm_marks"] * 0.4
#     )

#     df["engagement_score"] = (
#         df["attendance_percent"] * 0.6 +
#         df["study_hours_per_week"] * 5
#     )

#     return df


# def select_features(df):
#     X = df[["academic_score", "engagement_score"]]
#     y = df["final_result"]
#     return X, y











import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import sys
import os
 
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import (
    ACADEMIC_WEIGHTS, ENGAGEMENT_WEIGHTS,
    HIGH_RISK_SCORE, MEDIUM_RISK_SCORE
)
 
 
# ── STEP 1: CLEAN ─────────────────────────────────────────────────────────────
 
def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Remove duplicates and rows with missing values."""
    df = df.drop_duplicates()
    df = df.dropna()
    return df.reset_index(drop=True)
 
 
# ── STEP 2: FEATURE ENGINEERING ───────────────────────────────────────────────
 
def create_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create academic_score and engagement_score from raw columns.
    Weights come from config.py — single source of truth.
    """
    w = ACADEMIC_WEIGHTS
    e = ENGAGEMENT_WEIGHTS
 
    df["academic_score"] = (
        df["assignment_avg"]       * w["assignment_avg"]  +
        df["quiz_avg"]             * w["quiz_avg"]        +
        df["midterm_marks"]        * w["midterm_marks"]   +
        (df["study_hours_per_week"] * 5) * w["study_bonus"]
    ).round(2)
 
    df["engagement_score"] = (
        df["attendance_percent"]    * e["attendance_percent"] +
        df["study_hours_per_week"]  * e["study_hours_per_week"]
    ).round(2)
 
    return df
 
 
# ── STEP 3: SELECT FEATURES & TARGET ─────────────────────────────────────────
 
def select_features(df: pd.DataFrame):
    """Return X (features) and y (target) for model training."""
    X = df[["academic_score", "engagement_score"]]
    y = df["final_result"]
    return X, y
 
 
# ── STEP 4: SCALE (for Logistic Regression) ──────────────────────────────────
 
def scale_features(X_train, X_test):
    """
    StandardScaler fit on train, applied to both train and test.
    Required for Logistic Regression; optional for Random Forest.
    Returns scaled arrays and the fitted scaler (for later use in predict).
    """
    scaler  = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled  = scaler.transform(X_test)
    return X_train_scaled, X_test_scaled, scaler
 
 
# ── HELPER: RISK LABEL ────────────────────────────────────────────────────────
 
def get_risk_label(academic_score: float, attendance: float) -> str:
    """
    Single place to compute risk label.
    Used by app.py dashboard and any reporting tools.
    """
    if attendance < 50 or academic_score < HIGH_RISK_SCORE:
        return "High"
    elif academic_score < MEDIUM_RISK_SCORE:
        return "Medium"
    else:
        return "Low"
 
 
# ── HELPER: ENGINEER SINGLE STUDENT (for predict.py and app.py) ───────────────
 
def engineer_single(attendance: float, assignment: float,
                    quiz: float, midterm: float,
                    study_hours: float) -> list:
    """
    Compute [academic_score, engagement_score] for a single student.
    Returns a list ready to pass to model.predict().
    """
    w = ACADEMIC_WEIGHTS
    e = ENGAGEMENT_WEIGHTS
 
    academic = (
        assignment  * w["assignment_avg"]  +
        quiz        * w["quiz_avg"]        +
        midterm     * w["midterm_marks"]   +
        (study_hours * 5) * w["study_bonus"]
    )
 
    engagement = (
        attendance  * e["attendance_percent"] +
        study_hours * e["study_hours_per_week"]
    )
 
    return [[round(academic, 2), round(engagement, 2)]]