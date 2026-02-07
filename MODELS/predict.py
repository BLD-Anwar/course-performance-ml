import joblib
import numpy as np

print("Loading model...")

# Load trained model
model = joblib.load("student_performance_model.pkl")

print("Model loaded!")

# Example new student data
new_student = np.array([[75, 65, 70, 68, 3]])

print("Making prediction...")

prediction = model.predict(new_student)

print("Raw prediction value:", prediction)

if prediction[0] == 1:
    print("Prediction: Student is likely to PASS")
else:
    print("Prediction: Student is likely to FAIL")
