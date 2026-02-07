import sqlite3
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Connect to database
conn = sqlite3.connect("C:\\Users\\anwar\\OneDrive\\Desktop\\HACKATHON_3\\DATA\\university.db")

# Load data
query = "SELECT attendance_percent, assignment_avg, quiz_avg, midterm_marks, study_hours_per_week, final_result FROM course_performance"
df = pd.read_sql(query, conn)
conn.close()

# Features and target
X = df[["attendance_percent", "assignment_avg", "quiz_avg", "midterm_marks", "study_hours_per_week"]]
y = df["final_result"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Test model
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)

print(f"Model Accuracy: {accuracy * 100:.2f}%")

# Save model
joblib.dump(model, "student_performance_model.pkl")
print("Model saved successfully!")
