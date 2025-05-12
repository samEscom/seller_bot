import os

from fastapi import FastAPI

from app.routes import chat, health

app = FastAPI()

COMPANY_NAME = os.getenv("COMPANY_NAME", "la empresa")

app.include_router(chat.router)
app.include_router(health.router)


@app.get("/")
def read_root():
    return {"message": f"Hello from {COMPANY_NAME} Bot!"}
