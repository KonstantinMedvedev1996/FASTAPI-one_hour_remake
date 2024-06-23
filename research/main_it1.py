from fastapi import FastAPI
from pydantic import BaseModel
from typing_extensions import Optional

app = FastAPI()


class Task(BaseModel):
    name: str
    # description2: str | None
    description: Optional[str] = None

@app.get("/tasks")
def get_tasks():
    task = Task(name = "Download this video")
    return {"data": task}

@app.get("/")
def get_start():
    return "Begin first journey!"

@app.get("/home")
def get_home():
    return "Hello world!"


@app.get("/office")
def get_office():
    return {"data" : "Hello first job!"}
