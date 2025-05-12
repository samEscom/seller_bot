from fastapi import APIRouter

from app.request.chat import ChatRequest
from app.response.chat import ChatResponse
from app.services.llm import ask_gpt

router = APIRouter(
    prefix="/chat",
    tags=["chat"],
    responses={404: {"description": "Not found"}},
)


@router.post("/", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    response = ask_gpt(request.message)
    return ChatResponse(reply=response)
