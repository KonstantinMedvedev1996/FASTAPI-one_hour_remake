from typing import Annotated

from fastapi import FastAPI, Depends
from pydantic import BaseModel
from typing_extensions import Optional

from contextlib import asynccontextmanager

from database import create_tables, delete_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the ML model
    await delete_tables()
    print("Database is cleared")
    await create_tables()
    print("Database is ready")
    yield
    print("Shutting down")

    # Clean up the ML models and release the resources




app = FastAPI(lifespan = lifespan)


class STaskAdd(BaseModel):
    name: str
    description: Optional[str] = None

class STask(STaskAdd):
    id: int

tasks = []


@app.post("/tasks")
async def add_task(
        task: Annotated[STaskAdd, Depends()]

):
    tasks.append(task)
    return {"ok": True}


# @app.get("/tasks")
# def get_tasks():
#     task = Task(name = "Download this video")
#     return {"data": task}

