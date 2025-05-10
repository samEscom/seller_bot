from fastapi import APIRouter

from app.request.chat import ChatRequest
from app.response.chat import ChatResponse

router = APIRouter(
    prefix="/chat",
    tags=["chat"],
    responses={404: {"description": "Not found"}},
)


@router.post("/", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest):
    return ChatResponse(reply="Hello from the chat endpoint!")
