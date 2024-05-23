from fastapi import APIRouter

model_rooter = APIRouter(prefix="/models")


@model_rooter.get("/")
async def model():
    return {
        "message": "This is model page"
    }

@model_rooter.get("/model")
async def model_1():
    return {
        "message": "This is model page"
    }

@model_rooter.get("/model2")
async def model_2():
    return {
        "message": "This is model 2 page"
    }
