from fastapi import APIRouter

from .ai_chat_service.routes import router


v1_router = APIRouter()
v1_router.include_router(router, prefix="/chat", tags=["Chat"])