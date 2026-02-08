import sqlite3
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

print("Retraining model with latest database data...")

conn = sqlite3.connect("../data/university.db")
query = "SELECT attendance_percent, assignment_avg, quiz_avg, midterm_marks, study_hours_per_week, final_result FROM course_performance"
df = pd.read_sql(query, conn)
conn.close()

X = df[["attendance_percent", "assignment_avg", "quiz_avg", "midterm_marks", "study_hours_per_week"]]
y = df["final_result"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier()
model.fit(X_train, y_train)

predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)

print(f"New model accuracy: {accuracy * 100:.2f}%")

joblib.dump(model, "student_performance_model_latest.pkl")
print("Retrained model saved.")
