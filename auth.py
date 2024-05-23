from fastapi import APIRouter

auth_rooter = APIRouter(prefix="/auth")


@auth_rooter.get("/")
async def auth_1():
    return {
        "message": "This is auth page"
    }

@auth_rooter.get("/login")
async def auth_1():
    return {
        "message": "This is login page"
    }

@auth_rooter.get("/register")
async def auth_1():
    return {
        "message": "This is register page"
    }
