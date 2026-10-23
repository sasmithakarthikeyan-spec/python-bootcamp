from fastapi import FastAPI

app = FastAPI()

# Sample student data

students = [
    {"id": 1, "name": "Sash", "course": "Python"},
    {"id": 2, "name": "Ramesh", "course": "SQL"},
    {"id": 3, "name": "Kanya", "course": "Java"}
]


# GET: View all students
@app.get("/students")
def get_students():
    return students


from fastapi import FastAPI
from pydantic import BaseModel

#POST- add the student detail
class Student(BaseModel):
    id: int
    name: str
    course: str

@app.post("/students")
def add_student(student: Student):
    students.append(student.model_dump())
    return {
  "id": 3,
  "name": "Kanya",
  "course": "Java"
}

#PUT- update the data

@app.put("/students/{student_id}")
def update_student(student_id: int, updated_student: Student):
    for index, student in enumerate(students):
        if student["id"] == student_id:
            students[index] = updated_student.model_dump()
            return {
                "message": "Student updated successfully!",
                "student": students[index]
            }

    return {"message": "Student not found"}

#DELETE- delete a student

@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            return {
                "message": "Student deleted successfully!",
                "student": student
            }

    return {"message": "Student not found"}