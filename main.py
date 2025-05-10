import os

from fastapi import FastAPI

app = FastAPI()

COMPANY_NAME = os.getenv("COMPANY_NAME", "la empresa")


@app.get("/")
def read_root():
    return {"message": f"Hello from {COMPANY_NAME} Bot!"}
