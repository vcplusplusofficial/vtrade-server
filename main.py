from fastapi import FastAPI
from config import load_env_file
from models import users


load_env_file()

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


app.include_router(users.router, prefix="/user", tags=["user"])
