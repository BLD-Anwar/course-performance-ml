import joblib
import numpy as np

print("Loading trained model...")
model = joblib.load("student_performance_model.pkl")
print("Model loaded successfully!")

# -------------------------
# NEW STUDENT RAW DATA
# -------------------------
attendance = 75
assignment = 70
quiz = 65
midterm = 72
study_hours = 3

print("Making prediction for new student...")

# -------------------------
# CREATE SAME FEATURES AS TRAINING
# -------------------------

academic_score = (
    assignment * 0.3 +
    quiz * 0.3 +
    midterm * 0.4
)

engagement_score = (
    attendance * 0.6 +
    study_hours * 5
)

# Model expects 2 features
new_student = np.array([[academic_score, engagement_score]])

prediction = model.predict(new_student)

# -------------------------
# RESULT
# -------------------------
if prediction[0] == 1:
    print("Prediction: Student will PASS")
else:
    print("Prediction: Student will FAIL")
