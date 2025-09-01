

from fastapi import APIRouter, Depends
from app.services.ai_completition_service import ChatService
from core.dependencies.lifecycle import get_chat_service

router = APIRouter()

@router.get("/chat")
async def chat(
    query: str,
    chat_service: ChatService = Depends(get_chat_service)
):  
    response = await chat_service.get_response(query)
    return {"response": response}