from fastapi import FastAPI

app = FastAPI()

@app.post("/student")
def add_student():
    return {
        "message": "Student added successfully!",
        "name": "Sash",
        "course": "Python"
    }

@app.put("/student")
def update_student():
    return {
        "message": "Student updated successfully!",
        "name": "Sash",
        "course": "SQL"
    }

@app.delete("/student")
def delete_student():
    return {
        "message": "Student deleted successfully!",
        "name": "Sash"
    }