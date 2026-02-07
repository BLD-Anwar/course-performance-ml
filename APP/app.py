
import streamlit as st

st.title("Course Performance Monitoring System")

st.write("This dashboard will display student performance analytics and predictions.")

st.subheader("Prediction Module (Prototype)")

attendance = st.slider("Attendance Percentage", 0, 100, 75)
assignment = st.slider("Assignment Average", 0, 100, 65)
quiz = st.slider("Quiz Average", 0, 100, 70)
midterm = st.slider("Midterm Marks", 0, 100, 68)
study_hours = st.slider("Study Hours per Week", 0, 10, 3)

if st.button("Predict"):
    st.success("Prediction module connected to model will be implemented in next phase.")
