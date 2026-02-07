# import sqlite3
# import random

# conn = sqlite3.connect("university.db")
# cursor = conn.cursor()

# # Create tables (same as before)
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

# # Insert sample students
# students = [
#     (1, "Aman", "CSE", 2, 7.5),
#     (2, "Riya", "CSE", 2, 8.2),
#     (3, "Karan", "CSE", 2, 6.8),
#     (4, "Sneha", "CSE", 2, 9.1),
#     (5, "Arjun", "CSE", 2, 5.9)
# ]

# cursor.executemany("INSERT OR IGNORE INTO students VALUES (?, ?, ?, ?, ?)", students)

# # Insert one course
# cursor.execute("INSERT OR IGNORE INTO courses VALUES (1, 'Data Structures', 'CSE', 3)")

# # Insert course performance data
# for student_id in range(1, 6):
#     attendance = random.uniform(50, 100)
#     study_hours = random.uniform(1, 5)
#     assignment_avg = attendance * 0.4 + random.uniform(5, 15)
#     quiz_avg = study_hours * 10 + random.uniform(0, 10)
#     midterm_marks = assignment_avg * 0.5 + quiz_avg * 0.3 + random.uniform(0, 10)

#     # Pass/Fail logic
#     final_result = 1 if (attendance > 60 and midterm_marks > 40) else 0

#     cursor.execute("""
#     INSERT INTO course_performance 
#     (student_id, course_id, attendance_percent, assignment_avg, quiz_avg, midterm_marks, study_hours_per_week, final_result)
#     VALUES (?, ?, ?, ?, ?, ?, ?, ?)
#     """, (student_id, 1, attendance, assignment_avg, quiz_avg, midterm_marks, study_hours, final_result))

# conn.commit()
# conn.close()

# print("Sample data inserted successfully!")



import sqlite3
import random

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

cursor.execute("INSERT OR IGNORE INTO courses VALUES (1, 'Data Structures', 'CSE', 3)")

# ------------------ GENERATE STUDENTS ------------------

num_students = 200  # You can increase later

for student_id in range(1, num_students + 1):
    name = f"Student_{student_id}"
    department = "CSE"
    year = random.choice([1, 2, 3, 4])
    previous_gpa = round(random.uniform(5.0, 9.5), 2)

    cursor.execute("""
        INSERT OR IGNORE INTO students VALUES (?, ?, ?, ?, ?)
    """, (student_id, name, department, year, previous_gpa))

    # ------------------ PERFORMANCE LOGIC ------------------

    attendance = random.uniform(40, 100)
    study_hours = random.uniform(0.5, 5)

    # Students who attend more usually perform better
    assignment_avg = attendance * 0.4 + study_hours * 5 + random.uniform(0, 10)
    quiz_avg = study_hours * 12 + random.uniform(0, 10)
    midterm_marks = assignment_avg * 0.3 + quiz_avg * 0.4 + random.uniform(0, 10)

    # Final result logic (realistic)
    if attendance > 65 and midterm_marks > 45:
        final_result = 1  # Pass
    else:
        final_result = 0  # Fail

    cursor.execute("""
        INSERT INTO course_performance
        (student_id, course_id, attendance_percent, assignment_avg, quiz_avg, midterm_marks, study_hours_per_week, final_result)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (student_id, 1, attendance, assignment_avg, quiz_avg, midterm_marks, study_hours, final_result))

conn.commit()
conn.close()

print("Realistic synthetic data generated successfully!")
