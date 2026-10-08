'''import sqlite3
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

print("Database connection closed!")'''

#mini project
import sqlite3

connection = sqlite3.connect("student_management.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    course TEXT
)
""")

connection.commit()

print("Student Management System started!")

def add_student(name, age, course):
    cursor.execute("""
    INSERT INTO students (name, age, course)
    VALUES (?, ?, ?)
    """, (name, age, course))

    connection.commit()

    print(f"{name} added successfully!")

cursor.execute("SELECT COUNT(*) FROM students")
count = cursor.fetchone()[0]

if count == 0:
    add_student("Sasmitha", 19, "Python")
    add_student("Ramesh", 20, "SQL")
    add_student("Kanya", 19, "Java")

def display_students():
    cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()

    print("========================")
    print("ALL STUDENTS")
    print("========================")

    for student in students:
        print(f"ID: {student[0]}")
        print(f"Name: {student[1]}")
        print(f"Age: {student[2]}")
        print(f"Course: {student[3]}")
        print("------------------------")
display_students()

def search_student(name):
    cursor.execute("""
    SELECT * FROM students
    WHERE name = ?
    """, (name,))

    students = cursor.fetchall()

    if not students:
        print("Student not found!")
        return

    print("========================")
    print("SEARCH RESULTS")
    print("========================")

    for student in students:
        print(f"ID: {student[0]}")
        print(f"Name: {student[1]}")
        print(f"Age: {student[2]}")
        print(f"Course: {student[3]}")
        print("------------------------")
search_student("Sasmitha")

def update_student(student_id, new_course):
    cursor.execute("""
    UPDATE students
    SET course = ?
    WHERE id = ?
    """, (new_course, student_id))

    connection.commit()

    if cursor.rowcount == 0:
        print("Student not found!")
    else:
        print("Student updated successfully!")

update_student(3, "Python")

cursor.rowcount

def delete_student(student_id):
    cursor.execute("""
    DELETE FROM students
    WHERE id = ?
    """, (student_id,))

    connection.commit()

    if cursor.rowcount == 0:
        print("Student not found!")
    else:
        print("Student deleted successfully!")
delete_student(3)

while True:
    print("========================")
    print("STUDENT MANAGEMENT SYSTEM")
    print("========================")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        course = input("Enter course: ")

        add_student(name, age, course)

    elif choice == "2":
        display_students()

    elif choice == "3":
        name = input("Enter student name: ")
        search_student(name)

    elif choice == "4":
        student_id = int(input("Enter student ID: "))
        new_course = input("Enter new course: ")

        update_student(student_id, new_course)

    elif choice == "5":
        student_id = int(input("Enter student ID: "))

        delete_student(student_id)

    elif choice == "6":
        print("Exiting Student Management System...")
        break

    else:
        print("Invalid choice!")
