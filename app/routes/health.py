import os

import openai
from fastapi import APIRouter, HTTPException

from app.response.health import HealthOpenAiResponse, HealthResponse

router = APIRouter(
    prefix="/healthcheck",
    tags=["health"],
    responses={404: {"description": "Not found"}},
)


@router.get("")
async def api_check():
    return HealthResponse(status="ok")


@router.get("/openai")
async def api_check():
    try:
        openai.api_key = os.getenv("OPENAI_API_KEY")
        models = openai.models.list()
        return HealthOpenAiResponse(status="ok", model_count=len(models.data))

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
