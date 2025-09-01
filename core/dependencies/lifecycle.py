

from functools import lru_cache

from app.services.ai_completition_service import ChatService

@lru_cache(maxsize=1)
def get_chat_service() -> ChatService:
    return ChatService() 