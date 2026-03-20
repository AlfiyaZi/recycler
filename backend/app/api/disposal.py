from fastapi import APIRouter
from pydantic import BaseModel
from app.services.disposal_service import DisposalService

router = APIRouter()
disposal_service = DisposalService()


class DisposalRequest(BaseModel):
    item_name: str
    material: str
    country: str
    region: str | None = None


@router.post("/")
async def get_disposal_instructions(request: DisposalRequest):
    """Get location-specific disposal instructions for a detected item."""
    instructions = disposal_service.get_instructions(
        item_name=request.item_name,
        material=request.material,
        country=request.country,
        region=request.region,
    )
    return instructions
