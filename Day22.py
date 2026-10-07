import sqlite3
print("SQLite connected")
connection=sqlite3.connect("students.db")
print("database created and connected!")

cursor=connection.cursor()
print("Cursor created!")

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    course TEXT
)
""")

connection.commit()

print("Students table created!")
cursor.execute("SELECT * FROM students")

students_data = [
    ("Ramesh", 20, "SQL"),
    ("Kanya", 19, "Java"),
    ("Priya", 21, "Python")
]

cursor.executemany("""
INSERT INTO students (name, age, course)
VALUES (?, ?, ?)
""", students_data)

connection.commit()

print("Multiple students added!")

cursor.execute("SELECT * FROM students")

students = cursor.fetchall()

for student in students:
    print(student)

cursor.execute("""
SELECT * FROM students
WHERE course = ?
""", ("Python",))

python_students = cursor.fetchall()

print("PYTHON STUDENTS")

for student in python_students:
    print(student)

cursor.execute("""
UPDATE students
SET course = ?
WHERE name = ?
""", ("Python", "Kanya"))

connection.commit()

print("Student updated!")
cursor.execute("""
SELECT * FROM students
WHERE name = ?
""", ("Kanya",))

kanya = cursor.fetchall()

print("KANYA'S DETAILS")

for student in kanya:
    print(student)

cursor.execute("""
DELETE FROM students
WHERE id = ?
""", (4,))

connection.commit()

print("Student deleted!")

cursor.execute("SELECT * FROM students")

students = cursor.fetchall()

print("ALL STUDENTS")

for student in students:
    print(student)

connection.close()

print("Database connection closed!")