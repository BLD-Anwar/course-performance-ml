


import sys
import os

# Add parent directory to path if preprocessing is in a different location
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from preprocessing_p import clean_data, create_features, select_features


import sqlite3
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib




# Connect to database
conn = sqlite3.connect("C:\\Users\\anwar\\OneDrive\\Desktop\\HACKATHON_3\\DATA\\university.db")

# Load data
query = "SELECT attendance_percent, assignment_avg, quiz_avg, midterm_marks, study_hours_per_week, final_result FROM course_performance"
df = pd.read_sql(query, conn)
conn.close()

df = clean_data(df)
df = create_features(df)
X, y = select_features(df)


# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

model = RandomForestClassifier()
model.fit(X_train, y_train)

predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)

print(f"Random Forest Accuracy: {accuracy * 100:.2f}%")

# Train Logistic Regression
log_model = LogisticRegression(max_iter=1000)
log_model.fit(X_train, y_train)

log_predictions = log_model.predict(X_test)
log_accuracy = accuracy_score(y_test, log_predictions)

print(f"Logistic Regression Accuracy: {log_accuracy * 100:.2f}%")


# Test model
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)

print(f"Model Accuracy: {accuracy * 100:.2f}%")

# Save model
joblib.dump(model, "student_performance_model.pkl")
print("Model saved successfully!")
