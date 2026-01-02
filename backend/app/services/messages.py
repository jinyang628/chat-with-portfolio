import logging

from app.models.messages import MessageRequest, MessageResponse
from app.llm.gemini import LlmClient

log = logging.getLogger(__name__)


class MessagesService:
    async def chat(self, input: MessageRequest) -> MessageResponse:
        response = LlmClient().generate(input.content)
        return MessageResponse(id="123", content=response)
