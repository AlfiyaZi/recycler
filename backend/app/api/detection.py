from fastapi import APIRouter, UploadFile, File
from app.services.detection_service import DetectionService

router = APIRouter()
detection_service = DetectionService()


@router.post("/")
async def detect_items(image: UploadFile = File(...)):
    """Detect and classify waste items in an uploaded image."""
    image_bytes = await image.read()
    results = detection_service.detect(image_bytes)
    return {"items": results}
