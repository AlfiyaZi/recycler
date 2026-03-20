from fastapi import APIRouter
from pydantic import BaseModel
from app.services.chat_service import ChatService

router = APIRouter()
chat_service = ChatService()


class ChatRequest(BaseModel):
    question: str
    item_name: str | None = None
    material: str | None = None
    country: str | None = None


@router.post("/")
async def ask_followup(request: ChatRequest):
    """Ask a follow-up question about a scanned item."""
    answer = chat_service.ask(
        question=request.question,
        item_name=request.item_name,
        material=request.material,
        country=request.country,
    )
    return {"answer": answer}
