import time
from fastapi.responses import JSONResponse
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Error Handling API is running!"}

students = {
    1: "Sash",
    2: "Ramesh",
    3: "Kanya"
}

@app.get("/student/{student_id}")
def get_student(student_id: int):

    if student_id not in students:
        raise HTTPException(
            status_code=404,
            detail="Student not found!"
        )

    return {
        "student_id": student_id,
        "name": students[student_id]
    }

@app.get("/divide")
def divide(a: int, b: int):

    try:
        result = a / b

        return {
            "result": result
        }

    except ZeroDivisionError:
        raise HTTPException(
            status_code=400,
            detail="Cannot divide by zero!"
        )

@app.get("/check")
def check_error():

    try:
        print("Inside try block")

        result = 10 / 2

        return {
            "result": result
        }

    except ZeroDivisionError:
        raise HTTPException(
            status_code=400,
            detail="Cannot divide by zero!"
        )

    finally:
        print("Finally block executed")

@app.middleware("http")
async def my_middleware(request, call_next):

    print("Request received!")

    response = await call_next(request)

    print("Response sent!")

    return response

@app.middleware("http")
async def my_middleware(request, call_next):

    start_time = time.time()

    response = await call_next(request)

    end_time = time.time()

    process_time = end_time - start_time

    print(f"Response time: {process_time:.4f} seconds")

    return response

@app.exception_handler(Exception)
async def global_exception_handler(request, exc):

    return JSONResponse(
        status_code=500,
        content={
            "message": "Something went wrong!",
            "error": "Internal Server Error"
        }
    )
@app.get("/error")
def generate_error():
    raise RuntimeError("Testing global exception handler")