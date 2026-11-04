'''from fastapi import FastAPI, Depends

app = FastAPI()

def get_student():
    return {
        "name": "Sash",
        "course": "Python"
    }

@app.get("/student")
def student_details(student: dict = Depends(get_student)):
    return student

@app.get("/student-name")
def student_name(student: dict = Depends(get_student)):
    return {"student_name": student["name"]}


@app.get("/student-course")
def student_course(student: dict = Depends(get_student)):
    return {"student_course": student["course"]}

def get_student_info(name: str, course: str):
    return {
        "name": name,
        "course": course
    }


@app.get("/student-info")
def student_info(student: dict = Depends(get_student_info)):
    return student

def get_database():
    database = {
        "database_name": "StudentDB",
        "status": "Connected"
    }

    return database


@app.get("/database")
def database_details(db: dict = Depends(get_database)):
    return db

def get_connection():
    print("Database connection opened")

    yield "Database Connected"

    print("Database connection closed")


@app.get("/connection")
def connection_status(db=Depends(get_connection)):
    return {"status": db}'''

#mini project

from fastapi import FastAPI, Depends

app=FastAPI()

students=[
    {"id":1,"name":"Sasmitha","course":"Python"},
    {"id":2,"name":"Ramesh","course":"SQL"},
    {"id":3,"name":"Kanya","course":"Java"}
]

#Dependency function
def get_students():
    return students

#Get all students
@app.get("/students")
def all_students(data:list=Depends(get_students)):
    return data

#Get students by ID
def find_student(student_id:int,data:list=Depends(get_students)):
    for student in data:
        if student["id"]==student_id:
            return student

    return {"message":"Student not found"}

@app.get("/students/{student_id}")
def student_details(student:dict=Depends(find_student)):
    return student