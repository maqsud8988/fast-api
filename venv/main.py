from fastapi import FastAPI
from auth import auth_rooter

app = FastAPI()
app.include_router(auth_rooter)

@app.get("/")
async def test2():
    return {
        "message": "This is test page"
    }

@app.get("/test")
async def intro():
    return {
        "message": "HI lazy developers"
    }

@app.get("test_2")
async def test2():
    return {
        "message": "This is test page"
    }