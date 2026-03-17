# import sqlite3
# import pandas as pd
# from sklearn.ensemble import RandomForestClassifier
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score
# import joblib

# print("Retraining model with latest database data...")

# conn = sqlite3.connect("../data/university.db")
# query = "SELECT attendance_percent, assignment_avg, quiz_avg, midterm_marks, study_hours_per_week, final_result FROM course_performance"
# df = pd.read_sql(query, conn)
# conn.close()

# X = df[["attendance_percent", "assignment_avg", "quiz_avg", "midterm_marks", "study_hours_per_week"]]
# y = df["final_result"]

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# model = RandomForestClassifier()
# model.fit(X_train, y_train)

# predictions = model.predict(X_test)
# accuracy = accuracy_score(y_test, predictions)

# print(f"New model accuracy: {accuracy * 100:.2f}%")

# joblib.dump(model, "student_performance_model_latest.pkl")
# print("Retrained model saved.")















import sqlite3
import pandas as pd
import joblib
import sys
import os
from datetime import datetime
 
from sklearn.ensemble        import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics         import (accuracy_score, recall_score,
                                      precision_score, f1_score)
 
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import (DB_PATH, MODEL_PATH, MODELS_DIR,
                    RANDOM_STATE, TEST_SIZE, N_ESTIMATORS)
from preprocessing_p import clean_data, create_features, select_features
 
# ── LOAD LATEST DATA ──────────────────────────────────────────────────────────
print("📂  Loading latest data from database...")
conn = sqlite3.connect(DB_PATH)
df   = pd.read_sql(
    "SELECT attendance_percent, assignment_avg, quiz_avg, "
    "midterm_marks, study_hours_per_week, final_result "
    "FROM course_performance",
    conn
)
conn.close()
print(f"    Loaded {len(df)} records.")
 
# ── PREPROCESS ────────────────────────────────────────────────────────────────
# Uses SAME preprocessing as train_model.py — no feature mismatch
df   = clean_data(df)
df   = create_features(df)          # ← this was missing in original
X, y = select_features(df)          # ← academic_score, engagement_score
 
print(f"    Class balance: Pass={y.sum()} | Fail={len(y)-y.sum()}")
 
# ── SPLIT ─────────────────────────────────────────────────────────────────────
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=TEST_SIZE, random_state=RANDOM_STATE, stratify=y
)
 
# ── TRAIN ─────────────────────────────────────────────────────────────────────
print("\n🔄  Retraining Random Forest...")
model = RandomForestClassifier(n_estimators=N_ESTIMATORS, random_state=RANDOM_STATE)
model.fit(X_train, y_train)
 
# ── EVALUATE ──────────────────────────────────────────────────────────────────
preds = model.predict(X_test)
 
acc  = accuracy_score(y_test, preds)
rec  = recall_score(y_test, preds, pos_label=0)
prec = precision_score(y_test, preds, pos_label=0, zero_division=0)
f1   = f1_score(y_test, preds, pos_label=0, zero_division=0)
 
print(f"\n── Retrained Model Evaluation ──")
print(f"   Accuracy  : {acc*100:.2f}%")
print(f"   Recall    : {rec*100:.2f}%  ← (failing students caught)")
print(f"   Precision : {prec*100:.2f}%")
print(f"   F1 Score  : {f1*100:.2f}%")
 
# ── SAVE ──────────────────────────────────────────────────────────────────────
# 1. Save timestamped version so you can compare across retrains
timestamp        = datetime.now().strftime("%Y%m%d_%H%M%S")
versioned_path   = MODELS_DIR / f"student_performance_model_{timestamp}.pkl"
joblib.dump(model, versioned_path)
print(f"\n✅  Versioned model saved : {versioned_path}")
 
# 2. Overwrite main model so app.py picks up the latest automatically
joblib.dump(model, MODEL_PATH)
print(f"✅  Main model updated    : {MODEL_PATH}")