from fastapi import FastAPI
from auth import auth_rooter

app = FastAPI()
app.include_router(auth_rooter)

@app.get("/")
async def landing():
    return {
        "message": "This is landing page"
    }

@app.get("/user")
async def intro():
    return {
        "message": "this is user page"
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