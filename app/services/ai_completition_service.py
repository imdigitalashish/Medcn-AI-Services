
from pydantic_ai import Agent

class ChatService:
    
    def __init__(self) -> None:
        self.agent = Agent("google-gla:gemini-2.5-flash")
    
    async def get_response(self, query):
        response = await self.agent.run(query)
        return response.output