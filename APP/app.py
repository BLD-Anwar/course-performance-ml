import streamlit as st
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import joblib
import numpy as np
import os

st.title("Course Performance Monitoring Dashboard")

# --------------------------------------------------
# FIXED PATH HANDLING
# --------------------------------------------------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
db_path = os.path.join(BASE_DIR, "data", "university.db")
model_path = os.path.join(BASE_DIR, "models", "student_performance_model.pkl")

# --------------------------------------------------
# LOAD DATA FROM DATABASE
# --------------------------------------------------
conn = sqlite3.connect(db_path)
df = pd.read_sql("SELECT * FROM course_performance", conn)
conn.close()

st.subheader("Dataset Preview")
st.dataframe(df.head())

# --------------------------------------------------
# PASS VS FAIL DISTRIBUTION
# --------------------------------------------------
st.subheader("Pass vs Fail Distribution")
pass_fail_counts = df["final_result"].value_counts()
st.bar_chart(pass_fail_counts)

# --------------------------------------------------
# ATTENDANCE DISTRIBUTION
# --------------------------------------------------
st.subheader("Attendance Distribution")
fig1, ax1 = plt.subplots()
ax1.hist(df["attendance_percent"], bins=10)
ax1.set_xlabel("Attendance %")
ax1.set_ylabel("Number of Students")
st.pyplot(fig1)

# --------------------------------------------------
# AVERAGE SCORES
# --------------------------------------------------
st.subheader("Average Academic Scores")
st.write(f"Average Assignment Score: {df['assignment_avg'].mean():.2f}")
st.write(f"Average Quiz Score: {df['quiz_avg'].mean():.2f}")
st.write(f"Average Midterm Marks: {df['midterm_marks'].mean():.2f}")

# --------------------------------------------------
# PREDICTION MODULE
# --------------------------------------------------
st.markdown("---")
st.header("Student Pass/Fail Prediction")

attendance = st.slider("Attendance Percentage", 0, 100, 75)
assignment = st.slider("Assignment Average", 0, 100, 65)
quiz = st.slider("Quiz Average", 0, 100, 70)
midterm = st.slider("Midterm Marks", 0, 100, 68)
study_hours = st.slider("Study Hours per Week", 0, 10, 3)

if st.button("Predict Result"):
    try:
        model = joblib.load(model_path)
        input_data = np.array([[attendance, assignment, quiz, midterm, study_hours]])
        prediction = model.predict(input_data)

        if prediction[0] == 1:
            st.success("Prediction: Student is likely to PASS")
        else:
            st.error("Prediction: Student is likely to FAIL")

    except:
        st.warning("Model file not found. Please train the model first.")
