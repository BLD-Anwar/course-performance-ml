import sqlite3
import random

# ------------------ CONNECT DATABASE ------------------
conn = sqlite3.connect("university.db")
cursor = conn.cursor()

# ------------------ CREATE TABLES ------------------

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    student_id INTEGER PRIMARY KEY,
    name TEXT,
    department TEXT,
    year INTEGER,
    previous_gpa REAL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS courses (
    course_id INTEGER PRIMARY KEY,
    course_name TEXT,
    department TEXT,
    semester INTEGER
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS course_performance (
    record_id INTEGER PRIMARY KEY,
    student_id INTEGER,
    course_id INTEGER,
    attendance_percent REAL,
    assignment_avg REAL,
    quiz_avg REAL,
    midterm_marks REAL,
    study_hours_per_week REAL,
    final_result INTEGER
)
""")

# ------------------ INSERT COURSE ------------------

cursor.execute(
    "INSERT OR IGNORE INTO courses VALUES (1, 'Data Structures', 'CSE', 3)"
)

# ------------------ GENERATE STUDENTS ------------------

num_students = 200   # you can change this anytime

for student_id in range(1, num_students + 1):

    # ---------- student info ----------
    name = f"Student_{student_id}"
    department = "CSE"
    year = random.choice([1, 2, 3, 4])
    previous_gpa = round(random.uniform(5.0, 9.5), 2)

    cursor.execute("""
        INSERT OR IGNORE INTO students VALUES (?, ?, ?, ?, ?)
    """, (student_id, name, department, year, previous_gpa))

    # ---------- raw academic data (fully random) ----------
    attendance = round(random.uniform(40, 100), 2)
    study_hours = round(random.uniform(0.5, 6), 2)

    assignment_avg = round(random.uniform(30, 100), 2)
    quiz_avg = round(random.uniform(30, 100), 2)
    midterm_marks = round(random.uniform(30, 100), 2)

    # ---------- pass / fail rule ----------
    if attendance > 60 and midterm_marks > 50:
        final_result = 1
    else:
        final_result = 0

    # ---------- insert performance ----------
    cursor.execute("""
        INSERT INTO course_performance
        (student_id, course_id, attendance_percent,
         assignment_avg, quiz_avg, midterm_marks,
         study_hours_per_week, final_result)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        student_id,
        1,
        attendance,
        assignment_avg,
        quiz_avg,
        midterm_marks,
        study_hours,
        final_result
    ))

# ------------------ SAVE & CLOSE ------------------

conn.commit()
conn.close()

print("Random synthetic university data generated successfully!")
