from fastapi import FastAPI
from auth import auth_router
from pydantic import BaseModel
import uvicorn

app = FastAPI()


app = FastAPI()
app.include_router(auth_router)

@app.get("/")
async def landing():
    return {
        "message": "This is landing page"
    }

class UserRequest(BaseModel):
    name: str
    email: str

@app.get("/user")
async def intro():
    return {
        "message": "this is user page"
    }


@app.get("/items")
async def index():
    return {
        "message": "this is items page"
    }

@app.post("/items")
async def index():
    return {
        "message": "this is items request"
    }


@app.get("/user/{id}")
async def intro(id: int):
    return {
        "message": f"user - {id}"
    }


@app.post("/user")
async def intro():
    return {
        "message": "This is post request"
    }
















