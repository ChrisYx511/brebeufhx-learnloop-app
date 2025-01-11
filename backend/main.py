from fastapi import FastAPI, UploadFile

app = FastAPI()

@app.get("/upload_textbook")
def upload_textbook(file: UploadFile):
    # feed it through the API
    return {"message": "This is a test route!"}

@app.get("/get_next_video")
def get_next_video():
    return {"test": "test"}