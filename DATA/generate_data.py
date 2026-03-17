# import sqlite3
# import random

# # ------------------ CONNECT DATABASE ------------------
# conn = sqlite3.connect("university.db")
# cursor = conn.cursor()

# # ------------------ CREATE TABLES ------------------

# cursor.execute("""
# CREATE TABLE IF NOT EXISTS students (
#     student_id INTEGER PRIMARY KEY,
#     name TEXT,
#     department TEXT,
#     year INTEGER,
#     previous_gpa REAL
# )
# """)

# cursor.execute("""
# CREATE TABLE IF NOT EXISTS courses (
#     course_id INTEGER PRIMARY KEY,
#     course_name TEXT,
#     department TEXT,
#     semester INTEGER
# )
# """)

# cursor.execute("""
# CREATE TABLE IF NOT EXISTS course_performance (
#     record_id INTEGER PRIMARY KEY,
#     student_id INTEGER,
#     course_id INTEGER,
#     attendance_percent REAL,
#     assignment_avg REAL,
#     quiz_avg REAL,
#     midterm_marks REAL,
#     study_hours_per_week REAL,
#     final_result INTEGER
# )
# """)

# # ------------------ INSERT COURSE ------------------

# cursor.execute(
#     "INSERT OR IGNORE INTO courses VALUES (1, 'Data Structures', 'CSE', 3)"
# )

# # ------------------ GENERATE STUDENTS ------------------

# num_students = 200   # you can change this anytime

# for student_id in range(1, num_students + 1):

#     # ---------- student info ----------
#     name = f"Student_{student_id}"
#     department = "CSE"
#     year = random.choice([1, 2, 3, 4])
#     previous_gpa = round(random.uniform(5.0, 9.5), 2)

#     cursor.execute("""
#         INSERT OR IGNORE INTO students VALUES (?, ?, ?, ?, ?)
#     """, (student_id, name, department, year, previous_gpa))

#     # ---------- raw academic data (fully random) ----------
#     attendance = round(random.uniform(40, 100), 2)
#     study_hours = round(random.uniform(0.5, 6), 2)

#     assignment_avg = round(random.uniform(30, 100), 2)
#     quiz_avg = round(random.uniform(30, 100), 2)
#     midterm_marks = round(random.uniform(30, 100), 2)

#     # ---------- pass / fail rule ----------
#     if attendance > 60 and midterm_marks > 50:
#         final_result = 1
#     else:
#         final_result = 0

#     # ---------- insert performance ----------
#     cursor.execute("""
#         INSERT INTO course_performance
#         (student_id, course_id, attendance_percent,
#          assignment_avg, quiz_avg, midterm_marks,
#          study_hours_per_week, final_result)
#         VALUES (?, ?, ?, ?, ?, ?, ?, ?)
#     """, (
#         student_id,
#         1,
#         attendance,
#         assignment_avg,
#         quiz_avg,
#         midterm_marks,
#         study_hours,
#         final_result
#     ))

# # ------------------ SAVE & CLOSE ------------------

# conn.commit()
# conn.close()

# print("Random synthetic university data generated successfully!")























import sqlite3
import random
import numpy as np
import sys
import os
 
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import DB_PATH, PASS_THRESHOLD, ATTENDANCE_GATE
 
random.seed(42)
np.random.seed(42)
 
# ── CONNECT ───────────────────────────────────────────────────────────────────
conn   = sqlite3.connect(DB_PATH)
cursor = conn.cursor()
 
# ── CREATE TABLES ─────────────────────────────────────────────────────────────
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    student_id   INTEGER PRIMARY KEY,
    name         TEXT,
    department   TEXT,
    year         INTEGER,
    previous_gpa REAL
)""")
 
cursor.execute("""
CREATE TABLE IF NOT EXISTS courses (
    course_id   INTEGER PRIMARY KEY,
    course_name TEXT,
    department  TEXT,
    semester    INTEGER
)""")
 
cursor.execute("""
CREATE TABLE IF NOT EXISTS course_performance (
    record_id            INTEGER PRIMARY KEY,
    student_id           INTEGER,
    course_id            INTEGER,
    attendance_percent   REAL,
    assignment_avg       REAL,
    quiz_avg             REAL,
    midterm_marks        REAL,
    study_hours_per_week REAL,
    final_result         INTEGER
)""")
 
# ── CLEAR OLD DATA ────────────────────────────────────────────────────────────
cursor.execute("DELETE FROM course_performance")
cursor.execute("DELETE FROM students")
 
# ── SEED COURSE ───────────────────────────────────────────────────────────────
cursor.execute("INSERT OR IGNORE INTO courses VALUES (1, 'Data Structures', 'CSE', 3)")
 
# ── HELPER ────────────────────────────────────────────────────────────────────
def clamp(val, lo, hi):
    return max(lo, min(hi, val))
 
# ── GENERATE ──────────────────────────────────────────────────────────────────
NUM_STUDENTS = 200
pass_count   = 0
fail_count   = 0
 
for sid in range(1, NUM_STUDENTS + 1):
 
    # Student profile
    name         = f"Student_{sid}"
    department   = "CSE"
    year         = random.choice([1, 2, 3, 4])
    previous_gpa = round(random.uniform(5.0, 9.5), 2)
 
    cursor.execute(
        "INSERT OR IGNORE INTO students VALUES (?, ?, ?, ?, ?)",
        (sid, name, department, year, previous_gpa)
    )
 
    # ── STUDENT TYPE ─────────────────────────────────────────────────────
    # Each student has a base ability that drives ALL their scores.
    # This creates realistic correlations between features.
    roll = random.random()
    if roll < 0.35:
        student_type = "strong"      # 35%
    elif roll < 0.80:
        student_type = "average"     # 45%
    else:
        student_type = "weak"        # 20%
 
    if student_type == "strong":
        base_attendance  = random.uniform(75, 100)
        base_study_hours = random.uniform(3.5, 6.0)
        base_score       = random.uniform(65, 100)
    elif student_type == "average":
        base_attendance  = random.uniform(55, 85)
        base_study_hours = random.uniform(1.5, 4.0)
        base_score       = random.uniform(45, 80)
    else:
        base_attendance  = random.uniform(30, 65)
        base_study_hours = random.uniform(0.5, 2.5)
        base_score       = random.uniform(25, 60)
 
    # ── ADD NOISE ────────────────────────────────────────────────────────
    def noise(std=8):
        return np.random.normal(0, std)
 
    attendance    = clamp(round(base_attendance  + noise(5),   2), 0, 100)
    study_hours   = clamp(round(base_study_hours + noise(0.4), 2), 0.5, 8.0)
    assignment_avg = clamp(round(base_score      + noise(),    2), 0, 100)
    quiz_avg       = clamp(round(base_score      + noise(),    2), 0, 100)
    midterm_marks  = clamp(round(base_score - 5  + noise(),    2), 0, 100)
 
    # ── PASS / FAIL ───────────────────────────────────────────────────────
    # Uses all 5 features so the ML model can learn from each one.
    academic_score = (
        assignment_avg * 0.25 +
        quiz_avg       * 0.25 +
        midterm_marks  * 0.40 +
        (study_hours * 5) * 0.10
    )
 
    if attendance < ATTENDANCE_GATE:
        final_result = 0                          # attendance gate
    elif academic_score >= PASS_THRESHOLD:
        final_result = 1
    else:
        final_result = 0
 
    pass_count += final_result
    fail_count += (1 - final_result)
 
    cursor.execute("""
        INSERT INTO course_performance
        (student_id, course_id, attendance_percent,
         assignment_avg, quiz_avg, midterm_marks,
         study_hours_per_week, final_result)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (sid, 1, attendance, assignment_avg, quiz_avg,
          midterm_marks, study_hours, final_result))
 
# ── SAVE ──────────────────────────────────────────────────────────────────────
conn.commit()
conn.close()
 
print(f"✅  Data generated: {NUM_STUDENTS} students")
print(f"    Pass : {pass_count} ({pass_count/NUM_STUDENTS*100:.1f}%)")
print(f"    Fail : {fail_count} ({fail_count/NUM_STUDENTS*100:.1f}%)")
print(f"    DB   : {DB_PATH}")