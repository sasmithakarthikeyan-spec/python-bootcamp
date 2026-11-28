from fastapi import FastAPI

app= FastAPI(
    title="Sash Python API",
    description="My API documentatioon learning project",
    version="1.0.0"
)

@app.get(
    "/",
    summary="Home Page",
    description="Welcome users to my Python API.",
    tags=["General"]
)
def home():
    """
    Welcome users to my Python API
    """
    return {
        "message":"Welcome to Day 41!"
    }

@app.get(
    "/about",
    summary="About Page",
    description="Provides information about the developer.",
    tags=["Information"]
)

def about():
    """
    Provides information about the developer
    """
    return {
        "name":"Sash",
        "topic":"Documentation"
    }

def greet():
    """
    This functioon welcomes the user.
    """
    return "Hello Sash!"