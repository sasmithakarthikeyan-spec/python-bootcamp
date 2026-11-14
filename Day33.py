import os
import shutil

from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse

app = FastAPI()

@app.get("/")
def home():
    return {"message": "File Upload API is running!"}

@app.post("/upload")
def upload_file(file: UploadFile = File(...)):

    allowed_extensions = [".txt", ".pdf", ".png", ".jpg"]

    extension = os.path.splitext(file.filename)[1].lower()

    if extension not in allowed_extensions:
        return {
            "error": "File type not allowed!"
        }

    os.makedirs("uploads", exist_ok=True)

    file_path = os.path.join("uploads", file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    file.file.close()

    return {
        "message": "File uploaded successfully!",
        "filename": file.filename,
        "saved_path": file_path
    }

@app.get("/download/{filename}")
def download_file(filename: str):

    file_path = os.path.join("uploads", filename)

    if not os.path.exists(file_path):
        return {"message": "File not found!"}

    return FileResponse(
        path=file_path,
        filename=filename,
        media_type="application/octet-stream"
    )

@app.get("/files")
def list_files():

    files = os.listdir("uploads")

    return {
        "total_files": len(files),
        "files": files
    }