from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to my first API!"}

@app.get("/student")
def get_student():
    return {
        "name": "Sasmitha",
        "course": "Computer Science",
        "language": "Python"
    }

@app.get("/greet/{name}")
def greet_student(name: str):
    return {"message": f"Hello, {name}! Welcome to Python training."}

@app.get("/search")
def search_student(name: str, course: str):
    return {
        "student_name": name,
        "course": course,
        "message": f"Searching for {name} in {course}"
    }

@app.get("/add")
def add_numbers(a: int, b: int):
    return {
        "number1": a,
        "number2": b,
        "sum": a + b
    }