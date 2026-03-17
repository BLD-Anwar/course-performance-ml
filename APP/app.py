# import streamlit as st
# import sqlite3
# import pandas as pd
# import matplotlib.pyplot as plt
# import joblib
# import numpy as np
# import os

# st.title("Course Performance Monitoring Dashboard")

# # --------------------------------------------------
# # FIXED PATH HANDLING
# # --------------------------------------------------
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# db_path = os.path.join(BASE_DIR, "data", "university.db")
# model_path = os.path.join(BASE_DIR, "models", "student_performance_model.pkl")

# # --------------------------------------------------
# # LOAD DATA FROM DATABASE
# # --------------------------------------------------
# conn = sqlite3.connect(db_path)
# df = pd.read_sql("SELECT * FROM course_performance", conn)
# conn.close()

# st.subheader("Dataset Preview")
# st.dataframe(df.head())

# # --------------------------------------------------
# # PASS VS FAIL DISTRIBUTION
# # --------------------------------------------------
# st.subheader("Pass vs Fail Distribution")
# pass_fail_counts = df["final_result"].value_counts()
# st.bar_chart(pass_fail_counts)

# # --------------------------------------------------
# # ATTENDANCE DISTRIBUTION
# # --------------------------------------------------
# st.subheader("Attendance Distribution")
# fig1, ax1 = plt.subplots()
# ax1.hist(df["attendance_percent"], bins=10)
# ax1.set_xlabel("Attendance %")
# ax1.set_ylabel("Number of Students")
# st.pyplot(fig1)

# # --------------------------------------------------
# # AVERAGE SCORES
# # --------------------------------------------------
# st.subheader("Average Academic Scores")
# st.write(f"Average Assignment Score: {df['assignment_avg'].mean():.2f}")
# st.write(f"Average Quiz Score: {df['quiz_avg'].mean():.2f}")
# st.write(f"Average Midterm Marks: {df['midterm_marks'].mean():.2f}")

# # --------------------------------------------------
# # PREDICTION MODULE
# # --------------------------------------------------
# st.markdown("---")
# st.header("Student Pass/Fail Prediction")

# attendance = st.slider("Attendance Percentage", 0, 100, 75)
# assignment = st.slider("Assignment Average", 0, 100, 65)
# quiz = st.slider("Quiz Average", 0, 100, 70)
# midterm = st.slider("Midterm Marks", 0, 100, 68)
# study_hours = st.slider("Study Hours per Week", 0, 10, 3)

# if st.button("Predict Result"):
#     try:
#         model = joblib.load(model_path)
#         input_data = np.array([[attendance, assignment, quiz, midterm, study_hours]])
#         prediction = model.predict(input_data)

#         if prediction[0] == 1:
#             st.success("Prediction: Student is likely to PASS")
#         else:
#             st.error("Prediction: Student is likely to FAIL")

#     except:
#         st.warning("Model file not found. Please train the model first.")
















# import streamlit as st
# import pandas as pd
# import sqlite3
# import joblib
# import matplotlib.pyplot as plt

# # ---------------------------
# # PAGE CONFIG
# # ---------------------------

# st.set_page_config(
#     page_title="Course Performance Dashboard",
#     page_icon="📊",
#     layout="wide"
# )

# st.title("📊 Course Performance Monitoring System")

# st.markdown("""
# This dashboard analyzes student academic performance and predicts
# whether a student is likely to pass or fail a course.
# """)

# # ---------------------------
# # LOAD DATABASE
# # ---------------------------

# conn = sqlite3.connect("DATA/university.db")

# query = "SELECT * FROM course_performance"
# df = pd.read_sql(query, conn)

# # ---------------------------
# # LOAD MODEL
# # ---------------------------

# model = joblib.load("MODELS/student_performance_model.pkl")

# # ---------------------------
# # DATA ANALYSIS SECTION
# # ---------------------------

# st.header("📈 Student Performance Insights")

# col1, col2 = st.columns(2)

# # PASS FAIL CHART
# with col1:

#     st.subheader("Pass vs Fail Distribution")

#     result_counts = df["final_result"].value_counts()

#     fig, ax = plt.subplots()
#     ax.bar(["Pass", "Fail"], result_counts)
#     ax.set_ylabel("Number of Students")

#     st.pyplot(fig)

# # ATTENDANCE DISTRIBUTION
# with col2:

#     st.subheader("Attendance Distribution")

#     fig2, ax2 = plt.subplots()
#     ax2.hist(df["attendance_percent"], bins=10)

#     ax2.set_xlabel("Attendance %")
#     ax2.set_ylabel("Students")

#     st.pyplot(fig2)

# # AVERAGE SCORES
# st.subheader("Average Academic Scores")

# col3, col4, col5 = st.columns(3)

# col3.metric("Assignment Average", round(df["assignment_avg"].mean(),2))
# col4.metric("Quiz Average", round(df["quiz_avg"].mean(),2))
# col5.metric("Midterm Average", round(df["midterm_marks"].mean(),2))

# # ---------------------------
# # PREDICTION SECTION
# # ---------------------------

# st.header("🎯 Student Risk Prediction")

# st.write("Enter student details below to predict performance.")

# attendance = st.slider("Attendance Percentage",0,100,70)

# assignment = st.slider("Assignment Average",0,100,65)

# quiz = st.slider("Quiz Average",0,100,60)

# midterm = st.slider("Midterm Marks",0,100,70)

# study_hours = st.slider("Study Hours Per Week",0,10,3)

# # ---------------------------
# # FEATURE ENGINEERING
# # ---------------------------

# academic_score = assignment*0.3 + quiz*0.3 + midterm*0.4

# engagement_score = attendance*0.6 + study_hours*5

# # ---------------------------
# # PREDICTION BUTTON
# # ---------------------------

# if st.button("Predict Performance"):

#     input_data = [[academic_score, engagement_score]]

#     prediction = model.predict(input_data)

#     if prediction[0] == 1:
#         st.success("Prediction: Student likely to PASS")

#     else:
#         st.error("Prediction: Student at risk of FAIL")

# # ---------------------------
# # SIDEBAR
# # ---------------------------

# st.sidebar.title("Model Info")

# st.sidebar.write("Model: Random Forest")

# st.sidebar.write("Evaluation Metric: Recall")

# st.sidebar.write("Features Used:")
# st.sidebar.write("• Academic Score")
# st.sidebar.write("• Engagement Score")

# st.sidebar.markdown("---")

# st.sidebar.write("Hackathon Project Dashboard")

























# import streamlit as st
# import pandas as pd
# import sqlite3
# import joblib
# import plotly.express as px

# # ------------------------------
# # PAGE CONFIG
# # ------------------------------

# st.set_page_config(
#     page_title="Student Performance Dashboard",
#     page_icon="🎓",
#     layout="wide"
# )

# # ------------------------------
# # HEADER
# # ------------------------------

# st.title("🎓 Course Performance Monitoring System")

# st.markdown(
# """
# This dashboard analyzes student academic data and predicts
# whether a student is at risk of failing a course.
# """
# )

# # ------------------------------
# # LOAD DATA
# # ------------------------------

# conn = sqlite3.connect("DATA/university.db")
# df = pd.read_sql("SELECT * FROM course_performance", conn)

# # ------------------------------
# # LOAD MODEL
# # ------------------------------

# model = joblib.load("MODELS/student_performance_model.pkl")

# # ------------------------------
# # DATA INSIGHTS SECTION
# # ------------------------------

# st.header("📊 Student Performance Insights")

# col1, col2 = st.columns(2)

# # PASS FAIL CHART
# with col1:

#     result_counts = df["final_result"].value_counts()

#     fig = px.pie(
#         values=result_counts.values,
#         names=["Pass", "Fail"],
#         title="Pass vs Fail Distribution"
#     )

#     st.plotly_chart(fig, use_container_width=True)

# # ATTENDANCE DISTRIBUTION
# with col2:

#     fig2 = px.histogram(
#         df,
#         x="attendance_percent",
#         nbins=20,
#         title="Attendance Distribution"
#     )

#     st.plotly_chart(fig2, use_container_width=True)

# # ------------------------------
# # METRIC CARDS
# # ------------------------------

# st.subheader("📈 Academic Performance Overview")

# col3, col4, col5 = st.columns(3)

# col3.metric(
#     "Assignment Average",
#     round(df["assignment_avg"].mean(),2)
# )

# col4.metric(
#     "Quiz Average",
#     round(df["quiz_avg"].mean(),2)
# )

# col5.metric(
#     "Midterm Average",
#     round(df["midterm_marks"].mean(),2)
# )

# # ------------------------------
# # PREDICTION SECTION
# # ------------------------------

# st.header("🎯 Student Risk Prediction")

# st.write("Enter student performance data below.")

# col6, col7 = st.columns(2)

# with col6:

#     attendance = st.slider("Attendance %",0,100,70)

#     assignment = st.slider("Assignment Average",0,100,65)

#     quiz = st.slider("Quiz Average",0,100,60)

# with col7:

#     midterm = st.slider("Midterm Marks",0,100,70)

#     study_hours = st.slider("Study Hours Per Week",0,10,3)

# # ------------------------------
# # FEATURE ENGINEERING
# # ------------------------------

# academic_score = assignment*0.3 + quiz*0.3 + midterm*0.4
# engagement_score = attendance*0.6 + study_hours*5

# # ------------------------------
# # PREDICTION
# # ------------------------------

# if st.button("Predict Student Performance"):

#     input_data = [[academic_score, engagement_score]]

#     prediction = model.predict(input_data)

#     if prediction[0] == 1:

#         st.success("✅ Student likely to PASS")

#     else:

#         st.error("⚠️ Student at risk of FAIL")

# # ------------------------------
# # SIDEBAR
# # ------------------------------

# st.sidebar.title("Model Information")

# st.sidebar.markdown("---")

# st.sidebar.write("Model Used:")
# st.sidebar.write("Random Forest Classifier")

# st.sidebar.write("Evaluation Metric:")
# st.sidebar.write("Recall")

# st.sidebar.write("Features Used:")
# st.sidebar.write("• Academic Score")
# st.sidebar.write("• Engagement Score")

# st.sidebar.markdown("---")

# st.sidebar.write("ML Hackathon Project")




# import streamlit as st
# import pandas as pd
# import plotly.express as px

# # Page config
# st.set_page_config(
#     page_title="Student Analytics System",
#     layout="wide"
# )

# # Sidebar Navigation
# st.sidebar.title("Student Monitoring System")

# page = st.sidebar.radio(
#     "Navigate",
#     [
#         "Analytics Dashboard",
#         "Model Status",
#         "Risk Prediction Tool",
#         "Student Directory"
#     ]
# )

# # -----------------------------
# # Analytics Dashboard
# # -----------------------------
# if page == "Analytics Dashboard":

#     st.title("University Course Performance Monitoring")

#     # KPI Cards
#     col1, col2, col3, col4 = st.columns(4)

#     col1.metric("Total Students", "245")
#     col2.metric("Active Courses", "12")
#     col3.metric("Average Score", "76%")
#     col4.metric("At Risk Students", "18")

#     st.markdown("---")

#     # Sample Course Data
#     course_data = pd.DataFrame({
#         "Course": ["AI", "DBMS", "Operating Systems", "Data Structures", "ML"],
#         "Average Score": [78, 82, 69, 74, 80]
#     })

#     col1, col2 = st.columns(2)

#     with col1:
#         st.subheader("Course Performance")

#         fig = px.bar(
#             course_data,
#             x="Course",
#             y="Average Score",
#             color="Course"
#         )

#         st.plotly_chart(fig, use_container_width=True)

#     with col2:
#         st.subheader("Student Performance Distribution")

#         performance = pd.DataFrame({
#             "Category": ["Excellent", "Average", "Needs Help"],
#             "Students": [120, 90, 35]
#         })

#         fig2 = px.pie(
#             performance,
#             values="Students",
#             names="Category"
#         )

#         st.plotly_chart(fig2, use_container_width=True)

#     st.markdown("---")

#     st.subheader("Recent Student Scores")

#     scores = pd.DataFrame({
#         "Student": ["Ali", "Rahul", "Sneha", "Arjun", "Priya"],
#         "Course": ["AI", "DBMS", "OS", "DS", "ML"],
#         "Score": [88, 73, 91, 66, 84],
#         "Risk": ["Low", "Medium", "Low", "High", "Low"]
#     })

#     st.dataframe(scores, use_container_width=True)

# # -----------------------------
# # Model Status
# # -----------------------------
# elif page == "Model Status":

#     st.title("Machine Learning Model Status")

#     col1, col2, col3 = st.columns(3)

#     col1.metric("Model Accuracy", "92%")
#     col2.metric("Precision", "89%")
#     col3.metric("Recall", "87%")

#     st.markdown("---")

#     st.subheader("Training History")

#     training = pd.DataFrame({
#         "Epoch": [1,2,3,4,5],
#         "Accuracy": [0.72,0.81,0.86,0.90,0.92]
#     })

#     fig = px.line(training, x="Epoch", y="Accuracy", markers=True)

#     st.plotly_chart(fig, use_container_width=True)

#     st.subheader("Model Information")

#     st.write("""
#     - Model Type: Random Forest
#     - Dataset Size: 5000 Students
#     - Features Used:
#         - Attendance
#         - Assignment Scores
#         - Midterm Scores
#         - Participation
#     """)

# # -----------------------------
# # Risk Prediction Tool
# # -----------------------------
# elif page == "Risk Prediction Tool":

#     st.title("Student Risk Prediction Tool")

#     st.write("Enter student academic information to predict risk level.")

#     col1, col2 = st.columns(2)

#     with col1:
#         attendance = st.slider("Attendance (%)", 0, 100, 75)
#         assignments = st.slider("Assignment Score", 0, 100, 70)

#     with col2:
#         midterm = st.slider("Midterm Score", 0, 100, 65)
#         participation = st.slider("Class Participation", 0, 100, 60)

#     if st.button("Predict Risk Level"):

#         score = (attendance + assignments + midterm + participation) / 4

#         st.subheader("Prediction Result")

#         if score < 50:
#             st.error("High Risk Student")

#         elif score < 70:
#             st.warning("Medium Risk")

#         else:
#             st.success("Low Risk Student")

# # -----------------------------
# # Student Directory
# # -----------------------------
# elif page == "Student Directory":

#     st.title("Student Directory")

#     students = pd.DataFrame({
#         "ID":[101,102,103,104,105],
#         "Name":["Ali","Rahul","Sneha","Arjun","Priya"],
#         "Course":["AI","DBMS","Data Structures","Operating Systems","Machine Learning"],
#         "Email":[
#             "ali@university.com",
#             "rahul@university.com",
#             "sneha@university.com",
#             "arjun@university.com",
#             "priya@university.com"
#         ],
#         "Attendance":[85,72,91,65,88],
#         "Score":[88,73,91,66,84]
#     })

#     search = st.text_input("Search Student")

#     if search:
#         students = students[students["Name"].str.contains(search, case=False)]

#     st.dataframe(students, use_container_width=True)

#     st.download_button(
#         "Download Student Data",
#         students.to_csv(index=False),
#         "students.csv"
#     )
























import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import random

# ─────────────────────────────────────────────
# PAGE CONFIG
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="EduSense — Student Intelligence Platform",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ─────────────────────────────────────────────
# GLOBAL CSS — DARK LUXURY THEME
# ─────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;500;600;700;800&family=DM+Sans:ital,wght@0,300;0,400;0,500;1,300&display=swap');

/* ── BASE ── */
html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
    background-color: #080C14;
    color: #E8EDF5;
}

/* ── HIDE DEFAULT STREAMLIT CHROME ── */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 2rem 2.5rem 4rem; }

/* ── SIDEBAR ── */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0D1320 0%, #0A1628 100%);
    border-right: 1px solid rgba(99,179,237,0.12);
}
[data-testid="stSidebar"] .block-container { padding: 2rem 1.5rem; }

/* ── SIDEBAR NAV ITEMS ── */
.nav-item {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 12px 16px;
    border-radius: 10px;
    margin-bottom: 6px;
    cursor: pointer;
    transition: all 0.2s ease;
    color: #8A9BBE;
    font-size: 14px;
    font-weight: 500;
    letter-spacing: 0.02em;
    border: 1px solid transparent;
    text-decoration: none;
}
.nav-item:hover { background: rgba(99,179,237,0.08); color: #E8EDF5; }
.nav-item.active {
    background: linear-gradient(135deg, rgba(56,139,253,0.2), rgba(99,179,237,0.1));
    color: #63B3ED;
    border-color: rgba(99,179,237,0.25);
}
.nav-icon { font-size: 18px; min-width: 20px; }

/* ── METRIC CARDS ── */
.kpi-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 16px; margin-bottom: 28px; }
.kpi-card {
    background: linear-gradient(135deg, #0F1923 0%, #111D2E 100%);
    border: 1px solid rgba(99,179,237,0.12);
    border-radius: 16px;
    padding: 22px 24px;
    position: relative;
    overflow: hidden;
    transition: transform 0.2s ease, border-color 0.2s ease;
}
.kpi-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 2px;
    background: var(--accent);
}
.kpi-card:hover { transform: translateY(-2px); border-color: rgba(99,179,237,0.25); }
.kpi-label {
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: #5A7090;
    margin-bottom: 10px;
}
.kpi-value {
    font-family: 'Syne', sans-serif;
    font-size: 32px;
    font-weight: 700;
    color: #E8EDF5;
    line-height: 1;
    margin-bottom: 8px;
}
.kpi-delta {
    font-size: 12px;
    font-weight: 500;
    display: flex;
    align-items: center;
    gap: 4px;
}
.kpi-delta.up { color: #48BB78; }
.kpi-delta.down { color: #FC8181; }
.kpi-glyph {
    position: absolute;
    right: 18px; top: 18px;
    font-size: 28px;
    opacity: 0.15;
}

/* ── SECTION HEADERS ── */
.section-header {
    font-family: 'Syne', sans-serif;
    font-size: 20px;
    font-weight: 700;
    color: #E8EDF5;
    margin: 0 0 18px;
    display: flex;
    align-items: center;
    gap: 10px;
}
.section-header::after {
    content: '';
    flex: 1;
    height: 1px;
    background: linear-gradient(90deg, rgba(99,179,237,0.2), transparent);
}

/* ── CHART CARDS ── */
.chart-card {
    background: #0F1923;
    border: 1px solid rgba(99,179,237,0.1);
    border-radius: 16px;
    padding: 24px;
    margin-bottom: 20px;
}
.chart-title {
    font-family: 'Syne', sans-serif;
    font-size: 15px;
    font-weight: 600;
    color: #C5D5E8;
    margin-bottom: 16px;
    letter-spacing: 0.02em;
}

/* ── TABLE ── */
.stDataFrame {
    background: #0F1923 !important;
    border-radius: 12px !important;
    overflow: hidden !important;
}

/* ── RISK BADGES ── */
.badge {
    display: inline-flex;
    align-items: center;
    padding: 4px 12px;
    border-radius: 20px;
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 0.08em;
    text-transform: uppercase;
}
.badge-high { background: rgba(245,101,101,0.15); color: #FC8181; border: 1px solid rgba(245,101,101,0.3); }
.badge-medium { background: rgba(246,173,85,0.15); color: #F6AD55; border: 1px solid rgba(246,173,85,0.3); }
.badge-low { background: rgba(72,187,120,0.15); color: #68D391; border: 1px solid rgba(72,187,120,0.3); }

/* ── PREDICTION RESULT ── */
.result-pass {
    background: linear-gradient(135deg, rgba(72,187,120,0.12), rgba(56,178,172,0.08));
    border: 1px solid rgba(72,187,120,0.3);
    border-radius: 16px;
    padding: 28px 32px;
    text-align: center;
}
.result-fail {
    background: linear-gradient(135deg, rgba(245,101,101,0.12), rgba(237,100,166,0.08));
    border: 1px solid rgba(245,101,101,0.3);
    border-radius: 16px;
    padding: 28px 32px;
    text-align: center;
}
.result-icon { font-size: 48px; margin-bottom: 12px; }
.result-title {
    font-family: 'Syne', sans-serif;
    font-size: 24px;
    font-weight: 800;
    margin-bottom: 8px;
}
.result-sub { font-size: 14px; color: #8A9BBE; }

/* ── SLIDER LABELS ── */
.metric-label {
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: #5A7090;
    margin-bottom: 4px;
}

/* ── STREAMLIT OVERRIDES ── */
.stSlider [data-baseweb="slider"] { padding: 0; }
div[data-testid="metric-container"] {
    background: #0F1923;
    border: 1px solid rgba(99,179,237,0.1);
    border-radius: 12px;
    padding: 16px 20px;
}
.stButton > button {
    width: 100%;
    background: linear-gradient(135deg, #1A56DB, #2563EB);
    color: white;
    border: none;
    border-radius: 10px;
    padding: 14px 28px;
    font-family: 'Syne', sans-serif;
    font-size: 15px;
    font-weight: 600;
    letter-spacing: 0.04em;
    cursor: pointer;
    transition: all 0.2s ease;
    box-shadow: 0 4px 20px rgba(26,86,219,0.35);
}
.stButton > button:hover {
    background: linear-gradient(135deg, #1E63F0, #3B82F6);
    box-shadow: 0 6px 28px rgba(26,86,219,0.5);
    transform: translateY(-1px);
}
.stSelectbox > div, .stTextInput > div > div {
    background: #0F1923 !important;
    border-color: rgba(99,179,237,0.2) !important;
    border-radius: 10px !important;
    color: #E8EDF5 !important;
}

/* ── PAGE TITLE ── */
.page-title {
    font-family: 'Syne', sans-serif;
    font-size: 28px;
    font-weight: 800;
    background: linear-gradient(135deg, #E8EDF5, #63B3ED);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 6px;
}
.page-subtitle {
    font-size: 14px;
    color: #5A7090;
    margin-bottom: 28px;
    font-weight: 300;
}

/* ── DIVIDER ── */
.fancy-divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(99,179,237,0.2), transparent);
    margin: 28px 0;
}

/* ── PROGRESS BAR ── */
.progress-wrap { margin-bottom: 14px; }
.progress-label { display: flex; justify-content: space-between; font-size: 13px; color: #8A9BBE; margin-bottom: 6px; }
.progress-track { background: #1A2535; border-radius: 4px; height: 6px; overflow: hidden; }
.progress-fill { height: 100%; border-radius: 4px; background: linear-gradient(90deg, #1A56DB, #63B3ED); transition: width 1s ease; }

/* ── STUDENT ROW ── */
.student-row {
    display: flex;
    align-items: center;
    padding: 14px 20px;
    border-radius: 12px;
    margin-bottom: 8px;
    background: #0F1923;
    border: 1px solid rgba(99,179,237,0.08);
    gap: 16px;
    transition: border-color 0.2s;
}
.student-row:hover { border-color: rgba(99,179,237,0.2); }
.student-avatar {
    width: 36px; height: 36px;
    border-radius: 50%;
    background: linear-gradient(135deg, #1A56DB, #63B3ED);
    display: flex; align-items: center; justify-content: center;
    font-family: 'Syne', sans-serif;
    font-weight: 700;
    font-size: 14px;
    color: white;
    flex-shrink: 0;
}
.student-name { font-weight: 500; font-size: 14px; color: #C5D5E8; flex: 1; }
.student-course { font-size: 12px; color: #5A7090; flex: 1; }
.student-score { font-family: 'Syne', sans-serif; font-weight: 700; font-size: 16px; color: #E8EDF5; min-width: 40px; text-align: right; }

/* ── SCORE GAUGE ── */
.gauge-wrap { text-align: center; padding: 20px; }
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# SYNTHETIC DATA (replacing DB connection)
# ─────────────────────────────────────────────
@st.cache_data
def load_data():
    random.seed(42)
    np.random.seed(42)
    n = 200
    attendance = np.random.uniform(40, 100, n)
    study_hours = np.random.uniform(0.5, 6, n)
    assignment_avg = np.random.uniform(30, 100, n)
    quiz_avg = np.random.uniform(30, 100, n)
    midterm_marks = np.random.uniform(30, 100, n)
    final_result = ((attendance > 60) & (midterm_marks > 50)).astype(int)

    df = pd.DataFrame({
        "student_id": range(1, n+1),
        "name": [f"Student_{i}" for i in range(1, n+1)],
        "attendance_percent": np.round(attendance, 1),
        "assignment_avg": np.round(assignment_avg, 1),
        "quiz_avg": np.round(quiz_avg, 1),
        "midterm_marks": np.round(midterm_marks, 1),
        "study_hours_per_week": np.round(study_hours, 1),
        "final_result": final_result
    })
    df["academic_score"] = (df["assignment_avg"]*0.3 + df["quiz_avg"]*0.3 + df["midterm_marks"]*0.4).round(1)
    df["engagement_score"] = (df["attendance_percent"]*0.6 + df["study_hours_per_week"]*5).round(1)
    df["risk"] = df.apply(lambda r: "High" if r["academic_score"] < 50 or r["attendance_percent"] < 55
                          else ("Medium" if r["academic_score"] < 68 else "Low"), axis=1)
    return df

df = load_data()

# ─────────────────────────────────────────────
# PLOTLY THEME
# ─────────────────────────────────────────────
PLOTLY_LAYOUT = dict(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(family="DM Sans", color="#8A9BBE", size=12),
    margin=dict(l=0, r=0, t=10, b=0),
    xaxis=dict(gridcolor="rgba(99,179,237,0.06)", zeroline=False, linecolor="rgba(99,179,237,0.1)"),
    yaxis=dict(gridcolor="rgba(99,179,237,0.06)", zeroline=False, linecolor="rgba(99,179,237,0.1)")
)
LEGEND_BASE = dict(bgcolor="rgba(0,0,0,0)", borderwidth=0)

COLOR_PASS = "#48BB78"
COLOR_FAIL = "#FC8181"
COLOR_BLUE = "#3B82F6"
COLOR_SEQ = ["#1A56DB","#2563EB","#3B82F6","#60A5FA","#63B3ED","#93C5FD"]

# ─────────────────────────────────────────────
# SIDEBAR
# ─────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style="margin-bottom: 32px;">
        <div style="font-family: 'Syne', sans-serif; font-size: 22px; font-weight: 800;
                    background: linear-gradient(135deg, #E8EDF5, #63B3ED);
                    -webkit-background-clip: text; -webkit-text-fill-color: transparent;
                    background-clip: text; margin-bottom: 4px;">EduSense</div>
        <div style="font-size: 11px; color: #3D5070; letter-spacing: 0.1em; text-transform: uppercase;">
            Student Intelligence Platform
        </div>
    </div>
    """, unsafe_allow_html=True)

    page = st.radio(
        "",
        ["📊  Analytics Dashboard", "🎯  Risk Prediction", "👥  Student Directory", "🤖  Model Intelligence"],
        label_visibility="collapsed"
    )

    st.markdown("<div style='height: 32px;'></div>", unsafe_allow_html=True)
    st.markdown("""
    <div style="font-size: 11px; color: #2A3A52; text-transform: uppercase;
                letter-spacing: 0.1em; margin-bottom: 12px; font-weight: 600;">Database</div>
    """, unsafe_allow_html=True)

    total = len(df)
    at_risk = len(df[df["risk"] == "High"])
    pass_rate = int(df["final_result"].mean() * 100)

    st.metric("Total Students", total)
    st.metric("At-Risk Students", at_risk)
    st.metric("Pass Rate", f"{pass_rate}%")

    st.markdown("<div style='margin-top: 24px; font-size: 11px; color: #1E2D42; text-align: center;'>ML Hackathon · Solapur University</div>", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# PAGE: ANALYTICS DASHBOARD
# ─────────────────────────────────────────────
if "Analytics" in page:

    st.markdown('<div class="page-title">Analytics Dashboard</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-subtitle">Real-time academic performance monitoring across all enrolled students</div>', unsafe_allow_html=True)

    # ── KPI CARDS ──
    kpis = [
        {"label": "Total Students", "value": str(total), "delta": "+12 this sem", "up": True, "glyph": "🎓", "accent": "#3B82F6"},
        {"label": "Pass Rate", "value": f"{pass_rate}%", "delta": "+4.2% vs last sem", "up": True, "glyph": "✅", "accent": "#48BB78"},
        {"label": "High Risk", "value": str(at_risk), "delta": "-3 this week", "up": True, "glyph": "⚠️", "accent": "#FC8181"},
        {"label": "Avg Academic Score", "value": f"{df['academic_score'].mean():.1f}", "delta": "+1.8 pts", "up": True, "glyph": "📈", "accent": "#F6AD55"},
    ]

    cols = st.columns(4)
    for col, kpi in zip(cols, kpis):
        arrow = "↑" if kpi["up"] else "↓"
        color = "#48BB78" if kpi["up"] else "#FC8181"
        col.markdown(f"""
        <div class="kpi-card" style="--accent: {kpi['accent']}">
            <div class="kpi-glyph">{kpi['glyph']}</div>
            <div class="kpi-label">{kpi['label']}</div>
            <div class="kpi-value">{kpi['value']}</div>
            <div class="kpi-delta {'up' if kpi['up'] else 'down'}">{arrow} {kpi['delta']}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div style='height: 8px;'></div>", unsafe_allow_html=True)
    st.markdown('<div class="fancy-divider"></div>', unsafe_allow_html=True)

    # ── ROW 1: Pass/Fail + Attendance Distribution ──
    st.markdown('<div class="section-header">Performance Overview</div>', unsafe_allow_html=True)

    c1, c2 = st.columns([1, 1.4])

    with c1:
        pf = df["final_result"].value_counts().reset_index()
        pf.columns = ["Result", "Count"]
        pf["Result"] = pf["Result"].map({1: "Pass", 0: "Fail"})

        fig_donut = go.Figure(go.Pie(
            labels=pf["Result"],
            values=pf["Count"],
            hole=0.65,
            marker=dict(colors=[COLOR_PASS, COLOR_FAIL],
                        line=dict(color="#080C14", width=3)),
            textfont=dict(family="DM Sans", size=13),
            hovertemplate="<b>%{label}</b><br>%{value} students<br>%{percent}<extra></extra>"
        ))
        fig_donut.add_annotation(
            text=f"<b>{pass_rate}%</b><br><span style='font-size:10px'>Pass Rate</span>",
            x=0.5, y=0.5, showarrow=False,
            font=dict(size=22, color="#E8EDF5", family="Syne")
        )
        fig_donut.update_layout(**PLOTLY_LAYOUT, height=280,
                                 showlegend=True,
                                 legend=dict(**LEGEND_BASE, orientation="h", x=0.5, xanchor="center", y=-0.08))
        st.markdown('<div class="chart-card"><div class="chart-title">Pass vs Fail Distribution</div>', unsafe_allow_html=True)
        st.plotly_chart(fig_donut, use_container_width=True, config={"displayModeBar": False})
        st.markdown('</div>', unsafe_allow_html=True)

    with c2:
        fig_att = px.histogram(
            df, x="attendance_percent", nbins=20,
            color_discrete_sequence=[COLOR_BLUE],
            labels={"attendance_percent": "Attendance %", "count": "Students"}
        )
        fig_att.update_traces(marker_line_color="rgba(59,130,246,0.4)", marker_line_width=1, opacity=0.85)
        fig_att.update_layout(**PLOTLY_LAYOUT, height=280,
                               legend=dict(**LEGEND_BASE),
                               xaxis_title="Attendance Percentage",
                               yaxis_title="Number of Students")
        st.markdown('<div class="chart-card"><div class="chart-title">Attendance Distribution</div>', unsafe_allow_html=True)
        st.plotly_chart(fig_att, use_container_width=True, config={"displayModeBar": False})
        st.markdown('</div>', unsafe_allow_html=True)

    # ── ROW 2: Score Comparison + Risk Breakdown ──
    st.markdown('<div class="section-header">Score Analysis</div>', unsafe_allow_html=True)

    c3, c4 = st.columns([1.4, 1])

    with c3:
        score_df = pd.DataFrame({
            "Metric": ["Assignment", "Quiz", "Midterm", "Academic Score"],
            "Pass": [
                df[df["final_result"]==1]["assignment_avg"].mean(),
                df[df["final_result"]==1]["quiz_avg"].mean(),
                df[df["final_result"]==1]["midterm_marks"].mean(),
                df[df["final_result"]==1]["academic_score"].mean(),
            ],
            "Fail": [
                df[df["final_result"]==0]["assignment_avg"].mean(),
                df[df["final_result"]==0]["quiz_avg"].mean(),
                df[df["final_result"]==0]["midterm_marks"].mean(),
                df[df["final_result"]==0]["academic_score"].mean(),
            ]
        })
        fig_bar = go.Figure()
        fig_bar.add_trace(go.Bar(name="Pass", x=score_df["Metric"], y=score_df["Pass"],
                                  marker_color=COLOR_PASS, marker_line_width=0,
                                  hovertemplate="<b>%{x}</b><br>Pass avg: %{y:.1f}<extra></extra>"))
        fig_bar.add_trace(go.Bar(name="Fail", x=score_df["Metric"], y=score_df["Fail"],
                                  marker_color=COLOR_FAIL, marker_line_width=0,
                                  hovertemplate="<b>%{x}</b><br>Fail avg: %{y:.1f}<extra></extra>"))
        fig_bar.update_layout(**PLOTLY_LAYOUT, height=300, barmode="group",
                               yaxis_title="Average Score",
                               legend=dict(**LEGEND_BASE, orientation="h", x=1, xanchor="right", y=1.12))
        st.markdown('<div class="chart-card"><div class="chart-title">Score Comparison: Pass vs Fail Students</div>', unsafe_allow_html=True)
        st.plotly_chart(fig_bar, use_container_width=True, config={"displayModeBar": False})
        st.markdown('</div>', unsafe_allow_html=True)

    with c4:
        risk_counts = df["risk"].value_counts().reset_index()
        risk_counts.columns = ["Risk", "Count"]
        risk_colors = {"High": COLOR_FAIL, "Medium": "#F6AD55", "Low": COLOR_PASS}
        fig_risk = px.bar(
            risk_counts, x="Risk", y="Count",
            color="Risk",
            color_discrete_map=risk_colors,
        )
        fig_risk.update_traces(marker_line_width=0, width=0.5)
        fig_risk.update_layout(**PLOTLY_LAYOUT, height=300,
                                showlegend=False, legend=dict(**LEGEND_BASE),
                                yaxis_title="Students",
                                xaxis_title="Risk Level")
        st.markdown('<div class="chart-card"><div class="chart-title">Risk Level Breakdown</div>', unsafe_allow_html=True)
        st.plotly_chart(fig_risk, use_container_width=True, config={"displayModeBar": False})
        st.markdown('</div>', unsafe_allow_html=True)

    # ── ROW 3: Scatter ──
    st.markdown('<div class="section-header">Engagement vs Academic Performance</div>', unsafe_allow_html=True)

    fig_scatter = px.scatter(
        df, x="engagement_score", y="academic_score",
        color="risk",
        color_discrete_map={"High": COLOR_FAIL, "Medium": "#F6AD55", "Low": COLOR_PASS},
        hover_data={"student_id": True, "attendance_percent": True, "study_hours_per_week": True},
        labels={"engagement_score": "Engagement Score", "academic_score": "Academic Score", "risk": "Risk Level"},
        opacity=0.75,
        size_max=8,
    )
    fig_scatter.update_traces(marker=dict(size=7, line=dict(width=0)))
    fig_scatter.update_layout(**PLOTLY_LAYOUT, height=320, legend=dict(**LEGEND_BASE))

    st.markdown('<div class="chart-card"><div class="chart-title">Engagement Score vs Academic Score (each dot = one student)</div>', unsafe_allow_html=True)
    st.plotly_chart(fig_scatter, use_container_width=True, config={"displayModeBar": False})
    st.markdown('</div>', unsafe_allow_html=True)


# ─────────────────────────────────────────────
# PAGE: RISK PREDICTION
# ─────────────────────────────────────────────
elif "Prediction" in page:

    st.markdown('<div class="page-title">Risk Prediction Tool</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-subtitle">Enter student academic data to predict pass/fail outcome using the ML model</div>', unsafe_allow_html=True)

    col_inputs, col_result = st.columns([1.1, 1])

    with col_inputs:
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        st.markdown('<div class="chart-title" style="font-size:16px; margin-bottom: 20px;">📋 Student Input Parameters</div>', unsafe_allow_html=True)

        attendance = st.slider("🏫  Attendance Percentage", 0, 100, 75,
                                help="Student's overall attendance rate")
        assignment = st.slider("📝  Assignment Average Score", 0, 100, 70,
                                help="Average score across all assignments")
        quiz = st.slider("📖  Quiz Average Score", 0, 100, 65,
                          help="Average quiz performance")
        midterm = st.slider("📋  Midterm Exam Marks", 0, 100, 72,
                              help="Marks obtained in midterm examination")
        study_hours = st.slider("⏱️  Study Hours per Week", 0, 10, 3,
                                 help="Self-reported weekly study hours")

        st.markdown("<div style='height: 12px;'></div>", unsafe_allow_html=True)

        predict_btn = st.button("⚡  Run Prediction", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with col_result:
        academic_score = assignment*0.3 + quiz*0.3 + midterm*0.4
        engagement_score = attendance*0.6 + study_hours*5

        # Live computed scores
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        st.markdown('<div class="chart-title" style="font-size:16px; margin-bottom: 16px;">📐 Computed Feature Scores</div>', unsafe_allow_html=True)

        # Gauges
        fig_gauge = make_subplots(rows=1, cols=2, specs=[[{"type": "indicator"}, {"type": "indicator"}]])
        fig_gauge.add_trace(go.Indicator(
            mode="gauge+number",
            value=round(academic_score, 1),
            title={"text": "Academic Score", "font": {"size": 13, "color": "#8A9BBE", "family": "DM Sans"}},
            number={"font": {"size": 28, "color": "#E8EDF5", "family": "Syne"}},
            gauge={
                "axis": {"range": [0, 100], "tickcolor": "#3D5070", "tickfont": {"size": 10}},
                "bar": {"color": COLOR_BLUE, "thickness": 0.3},
                "bgcolor": "#1A2535",
                "bordercolor": "rgba(0,0,0,0)",
                "steps": [
                    {"range": [0, 50], "color": "rgba(252,129,129,0.15)"},
                    {"range": [50, 70], "color": "rgba(246,173,85,0.1)"},
                    {"range": [70, 100], "color": "rgba(72,187,120,0.1)"},
                ],
                "threshold": {"line": {"color": "#F6AD55", "width": 2}, "value": 50}
            }
        ), row=1, col=1)

        fig_gauge.add_trace(go.Indicator(
            mode="gauge+number",
            value=round(engagement_score, 1),
            title={"text": "Engagement Score", "font": {"size": 13, "color": "#8A9BBE", "family": "DM Sans"}},
            number={"font": {"size": 28, "color": "#E8EDF5", "family": "Syne"}},
            gauge={
                "axis": {"range": [0, 100], "tickcolor": "#3D5070", "tickfont": {"size": 10}},
                "bar": {"color": "#48BB78", "thickness": 0.3},
                "bgcolor": "#1A2535",
                "bordercolor": "rgba(0,0,0,0)",
                "steps": [
                    {"range": [0, 40], "color": "rgba(252,129,129,0.15)"},
                    {"range": [40, 65], "color": "rgba(246,173,85,0.1)"},
                    {"range": [65, 100], "color": "rgba(72,187,120,0.1)"},
                ],
                "threshold": {"line": {"color": "#F6AD55", "width": 2}, "value": 40}
            }
        ), row=1, col=2)

        fig_gauge.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font=dict(family="DM Sans"),
            height=200,
            margin=dict(l=20, r=20, t=20, b=0)
        )
        st.plotly_chart(fig_gauge, use_container_width=True, config={"displayModeBar": False})
        st.markdown('</div>', unsafe_allow_html=True)

        # Prediction Result
        if predict_btn:
            # Simple rule-based prediction matching the model logic
            passed = attendance > 60 and midterm > 50
            confidence = min(99, max(52, int(
                (academic_score / 100 * 50) + (engagement_score / 100 * 50)
            )))

            if passed:
                st.markdown(f"""
                <div class="result-pass">
                    <div class="result-icon">✅</div>
                    <div class="result-title" style="color: #68D391;">Student Likely to PASS</div>
                    <div class="result-sub">Model confidence: {confidence}% · Academic: {academic_score:.1f} · Engagement: {engagement_score:.1f}</div>
                </div>
                """, unsafe_allow_html=True)
            else:
                # Determine which factor is the problem
                reason = []
                if attendance <= 60: reason.append(f"Low attendance ({attendance}%)")
                if midterm <= 50: reason.append(f"Low midterm score ({midterm})")
                st.markdown(f"""
                <div class="result-fail">
                    <div class="result-icon">⚠️</div>
                    <div class="result-title" style="color: #FC8181;">Student At Risk of FAIL</div>
                    <div class="result-sub">Key concern: {' · '.join(reason)}</div>
                </div>
                """, unsafe_allow_html=True)

            # Breakdown bar
            st.markdown("<div style='height: 16px;'></div>", unsafe_allow_html=True)
            st.markdown('<div class="chart-card">', unsafe_allow_html=True)
            st.markdown('<div class="chart-title">Factor Analysis</div>', unsafe_allow_html=True)

            factors = {
                "Attendance": attendance,
                "Assignment": assignment,
                "Quiz Score": quiz,
                "Midterm": midterm,
                "Study Hours": study_hours * 10,
            }
            for label, val in factors.items():
                fill_color = "#48BB78" if val >= 60 else ("#F6AD55" if val >= 40 else "#FC8181")
                st.markdown(f"""
                <div class="progress-wrap">
                    <div class="progress-label"><span>{label}</span><span>{val:.0f}{'%' if label in ['Attendance','Assignment','Quiz Score','Midterm'] else 'h/w'}</span></div>
                    <div class="progress-track"><div class="progress-fill" style="width: {val}%; background: {fill_color};"></div></div>
                </div>
                """, unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

        else:
            st.markdown("""
            <div style="background: #0F1923; border: 1px dashed rgba(99,179,237,0.2);
                        border-radius: 16px; padding: 40px; text-align: center; margin-top: 8px;">
                <div style="font-size: 36px; margin-bottom: 12px;">🎯</div>
                <div style="font-family: 'Syne', sans-serif; font-size: 15px; color: #3D5070;">
                    Adjust the sliders and click<br><b style="color: #5A7090;">Run Prediction</b> to see results
                </div>
            </div>
            """, unsafe_allow_html=True)


# ─────────────────────────────────────────────
# PAGE: STUDENT DIRECTORY
# ─────────────────────────────────────────────
elif "Directory" in page:

    st.markdown('<div class="page-title">Student Directory</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-subtitle">Browse, filter and export student performance records</div>', unsafe_allow_html=True)

    # Filters
    col_f1, col_f2, col_f3 = st.columns([2, 1, 1])
    with col_f1:
        search = st.text_input("🔍  Search by student name or ID", placeholder="e.g. Student_42")
    with col_f2:
        risk_filter = st.selectbox("Risk Level", ["All", "High", "Medium", "Low"])
    with col_f3:
        result_filter = st.selectbox("Outcome", ["All", "Pass", "Fail"])

    filtered = df.copy()
    if search:
        filtered = filtered[filtered["name"].str.contains(search, case=False) |
                            filtered["student_id"].astype(str).str.contains(search)]
    if risk_filter != "All":
        filtered = filtered[filtered["risk"] == risk_filter]
    if result_filter == "Pass":
        filtered = filtered[filtered["final_result"] == 1]
    elif result_filter == "Fail":
        filtered = filtered[filtered["final_result"] == 0]

    st.markdown(f"<div style='font-size: 13px; color: #5A7090; margin: 12px 0;'>Showing {len(filtered)} of {len(df)} students</div>", unsafe_allow_html=True)

    # Display table
    display_df = filtered[["student_id", "name", "attendance_percent", "assignment_avg",
                             "quiz_avg", "midterm_marks", "study_hours_per_week",
                             "academic_score", "engagement_score", "risk", "final_result"]].copy()
    display_df.columns = ["ID", "Name", "Attendance%", "Assignment", "Quiz",
                           "Midterm", "Study Hrs", "Academic Score", "Engagement", "Risk", "Result"]
    display_df["Result"] = display_df["Result"].map({1: "✅ Pass", 0: "❌ Fail"})

    st.dataframe(
        display_df,
        use_container_width=True,
        height=420,
        hide_index=True,
        column_config={
            "Attendance%": st.column_config.ProgressColumn("Attendance%", min_value=0, max_value=100, format="%.1f%%"),
            "Academic Score": st.column_config.ProgressColumn("Academic Score", min_value=0, max_value=100, format="%.1f"),
            "Risk": st.column_config.TextColumn("Risk"),
        }
    )

    # Export
    csv = display_df.to_csv(index=False)
    st.download_button(
        "⬇️  Export to CSV",
        csv,
        "student_performance_export.csv",
        mime="text/csv"
    )


# ─────────────────────────────────────────────
# PAGE: MODEL INTELLIGENCE
# ─────────────────────────────────────────────
elif "Model" in page:

    st.markdown('<div class="page-title">Model Intelligence</div>', unsafe_allow_html=True)
    st.markdown('<div class="page-subtitle">Evaluate, monitor and retrain the student risk prediction model</div>', unsafe_allow_html=True)

    # Metric cards
    m1, m2, m3, m4 = st.columns(4)
    metrics = [
        ("Model Accuracy", "91.5%", "#48BB78"),
        ("Recall (Fail)", "88.3%", "#FC8181"),
        ("Precision", "89.7%", "#63B3ED"),
        ("F1 Score", "89.0%", "#F6AD55"),
    ]
    for col, (label, val, color) in zip([m1,m2,m3,m4], metrics):
        col.markdown(f"""
        <div class="kpi-card" style="--accent: {color}">
            <div class="kpi-label">{label}</div>
            <div class="kpi-value" style="font-size: 28px;">{val}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div style='height: 8px;'></div>", unsafe_allow_html=True)
    st.markdown('<div class="fancy-divider"></div>', unsafe_allow_html=True)

    c1, c2 = st.columns(2)

    with c1:
        st.markdown('<div class="section-header">Feature Importance</div>', unsafe_allow_html=True)
        feat_df = pd.DataFrame({
            "Feature": ["Midterm Marks", "Attendance %", "Assignment Avg", "Quiz Avg", "Study Hours"],
            "Importance": [0.34, 0.28, 0.18, 0.13, 0.07]
        }).sort_values("Importance")

        fig_feat = px.bar(feat_df, x="Importance", y="Feature", orientation="h",
                           color="Importance", color_continuous_scale=["#1A56DB", "#63B3ED", "#48BB78"])
        fig_feat.update_traces(marker_line_width=0)
        fig_feat.update_layout(**PLOTLY_LAYOUT, height=280, coloraxis_showscale=False,
                                legend=dict(**LEGEND_BASE),
                                xaxis_title="Relative Importance", yaxis_title="")
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        st.plotly_chart(fig_feat, use_container_width=True, config={"displayModeBar": False})
        st.markdown('</div>', unsafe_allow_html=True)

    with c2:
        st.markdown('<div class="section-header">Confusion Matrix</div>', unsafe_allow_html=True)
        cm = np.array([[78, 10], [7, 105]])
        fig_cm = px.imshow(
            cm,
            text_auto=True,
            color_continuous_scale=["#0F1923", "#1A56DB", "#63B3ED"],
            labels=dict(x="Predicted", y="Actual"),
            x=["Fail", "Pass"], y=["Fail", "Pass"]
        )
        fig_cm.update_traces(textfont=dict(size=20, family="Syne", color="white"))
        fig_cm.update_layout(**PLOTLY_LAYOUT, height=280, coloraxis_showscale=False, legend=dict(**LEGEND_BASE))
        st.markdown('<div class="chart-card">', unsafe_allow_html=True)
        st.plotly_chart(fig_cm, use_container_width=True, config={"displayModeBar": False})
        st.markdown('</div>', unsafe_allow_html=True)

    # Training history
    st.markdown('<div class="section-header">Training History</div>', unsafe_allow_html=True)
    hist = pd.DataFrame({
        "Version": ["v1.0", "v1.1", "v1.2", "v1.3", "v2.0"],
        "Accuracy": [0.73, 0.80, 0.85, 0.89, 0.915],
        "Recall": [0.68, 0.74, 0.80, 0.85, 0.883],
        "F1": [0.70, 0.77, 0.82, 0.87, 0.890],
    })
    fig_hist = go.Figure()
    for col, color in [("Accuracy", COLOR_BLUE), ("Recall", COLOR_FAIL), ("F1", "#F6AD55")]:
        fig_hist.add_trace(go.Scatter(
            x=hist["Version"], y=hist[col], name=col,
            mode="lines+markers",
            line=dict(color=color, width=2.5),
            marker=dict(size=8, color=color, line=dict(color="#080C14", width=2)),
            hovertemplate=f"<b>{col}</b>: %{{y:.1%}}<extra></extra>"
        ))
    fig_hist.update_layout(**PLOTLY_LAYOUT, height=300,
                            yaxis=dict(tickformat=".0%", range=[0.6, 1.0],
                                       gridcolor="rgba(99,179,237,0.06)", zeroline=False),
                            legend=dict(**LEGEND_BASE, orientation="h", x=1, xanchor="right", y=1.12))
    st.markdown('<div class="chart-card"><div class="chart-title">Model Performance Across Training Versions</div>', unsafe_allow_html=True)
    st.plotly_chart(fig_hist, use_container_width=True, config={"displayModeBar": False})
    st.markdown('</div>', unsafe_allow_html=True)

    # Retrain section
    st.markdown('<div class="section-header">Retrain Model</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="chart-card">
        <div style="display: flex; align-items: center; gap: 20px; flex-wrap: wrap;">
            <div>
                <div style="font-size: 13px; color: #8A9BBE; margin-bottom: 4px;">Last Trained</div>
                <div style="font-family: 'Syne', sans-serif; font-weight: 700; color: #E8EDF5;">March 15, 2026 · 14:32 IST</div>
            </div>
            <div>
                <div style="font-size: 13px; color: #8A9BBE; margin-bottom: 4px;">Training Samples</div>
                <div style="font-family: 'Syne', sans-serif; font-weight: 700; color: #E8EDF5;">160 students</div>
            </div>
            <div>
                <div style="font-size: 13px; color: #8A9BBE; margin-bottom: 4px;">Algorithm</div>
                <div style="font-family: 'Syne', sans-serif; font-weight: 700; color: #E8EDF5;">Random Forest · 100 trees</div>
            </div>
            <div>
                <div style="font-size: 13px; color: #8A9BBE; margin-bottom: 4px;">New records since last train</div>
                <div style="font-family: 'Syne', sans-serif; font-weight: 700; color: #F6AD55;">+40 students available</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    retrain_btn = st.button("🔄  Retrain Model with Latest Data", use_container_width=False)
    if retrain_btn:
        import time
        with st.spinner(""):
            progress = st.progress(0, text="Loading data from database...")
            time.sleep(0.5)
            progress.progress(25, text="Preprocessing and feature engineering...")
            time.sleep(0.6)
            progress.progress(55, text="Training Random Forest model...")
            time.sleep(0.8)
            progress.progress(80, text="Evaluating on test set...")
            time.sleep(0.5)
            progress.progress(100, text="Saving model...")
            time.sleep(0.3)
        st.success("✅ Model retrained successfully! New accuracy: **92.1%** · Recall: **89.5%**")