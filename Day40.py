from fastapi import FastAPI

app= FastAPI()

@app.get("/")
def home():
    return {
        "message":"Welcome to my deployed application"
    }

@app.get("/about")
def about():
    return{
        "name":"Sash",
        "course":"Python",
        "topic":"Deployment"
    }