# import joblib
# import numpy as np

# print("Loading trained model...")
# model = joblib.load("student_performance_model.pkl")
# print("Model loaded successfully!")

# # -------------------------
# # NEW STUDENT RAW DATA
# # -------------------------
# attendance = 75
# assignment = 70
# quiz = 65
# midterm = 72
# study_hours = 3

# print("Making prediction for new student...")

# # -------------------------
# # CREATE SAME FEATURES AS TRAINING
# # -------------------------

# academic_score = (
#     assignment * 0.3 +
#     quiz * 0.3 +
#     midterm * 0.4
# )

# engagement_score = (
#     attendance * 0.6 +
#     study_hours * 5
# )

# # Model expects 2 features
# new_student = np.array([[academic_score, engagement_score]])

# prediction = model.predict(new_student)

# # -------------------------
# # RESULT
# # -------------------------
# if prediction[0] == 1:
#     print("Prediction: Student will PASS")
# else:
#     print("Prediction: Student will FAIL")





 
import joblib
import sys
import os
 
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import MODEL_PATH
from preprocessing_p import engineer_single, get_risk_label
 
# ── LOAD MODEL ────────────────────────────────────────────────────────────────
print("📦  Loading model...")
model = joblib.load(MODEL_PATH)
print(f"    Loaded from: {MODEL_PATH}\n")
 
# ── INPUT: EDIT THESE VALUES ──────────────────────────────────────────────────
attendance   = 75
assignment   = 70
quiz         = 65
midterm      = 72
study_hours  = 3
 
# ── ENGINEER FEATURES ────────────────────────────────────────────────────────
# Imported from preprocessing_p — no duplication
import pandas as pd
raw      = engineer_single(attendance, assignment, quiz, midterm, study_hours)
features = pd.DataFrame(raw, columns=["academic_score", "engagement_score"])
academic_score    = features["academic_score"].iloc[0]
engagement_score  = features["engagement_score"].iloc[0]
 
print(f"── Computed Feature Scores ──")
print(f"   Academic Score    : {academic_score}")
print(f"   Engagement Score  : {engagement_score}")
 
# ── PREDICT ───────────────────────────────────────────────────────────────────
prediction = model.predict(features)[0]
 
# Confidence (probability of the predicted class)
proba      = model.predict_proba(features)[0]
confidence = round(max(proba) * 100, 1)
 
# Risk label
risk = get_risk_label(academic_score, attendance)
 
# ── RESULT ────────────────────────────────────────────────────────────────────
print(f"\n── Prediction Result ──")
if prediction == 1:
    print(f"   ✅  Student will PASS")
else:
    print(f"   ⚠️  Student at risk of FAIL")
 
print(f"   Confidence  : {confidence}%")
print(f"   Risk Level  : {risk}")