"""Detection Service — AI component.

Uses YOLO for object detection and material classification.
This is where AI and SE meet: the service wraps the AI model
with proper error handling, confidence thresholds, and structured output.
"""

from io import BytesIO
from PIL import Image

# Confidence threshold below which we tell the user we can't identify the item (Req07)
CONFIDENCE_THRESHOLD = 0.5


class DetectionService:
    def __init__(self):
        self._model = None

    def _load_model(self):
        """Lazy-load the YOLO model to avoid slow startup."""
        if self._model is None:
            from ultralytics import YOLO
            # TODO: replace with fine-tuned model on waste dataset
            self._model = YOLO("yolov8n.pt")

    def detect(self, image_bytes: bytes) -> list[dict]:
        """Detect waste items in an image.

        Returns a list of detected items with name, material, confidence,
        and bounding box. Items below the confidence threshold are filtered out.
        """
        self._load_model()
        image = Image.open(BytesIO(image_bytes))
        results = self._model(image)

        items = []
        for result in results:
            for box in result.boxes:
                confidence = float(box.conf[0])
                if confidence < CONFIDENCE_THRESHOLD:
                    continue
                class_id = int(box.cls[0])
                item_name = result.names[class_id]
                items.append({
                    "item_name": item_name,
                    "confidence": round(confidence, 3),
                    "material": self._classify_material(item_name),
                    "bbox": box.xyxy[0].tolist(),
                })

        return items

    def _classify_material(self, item_name: str) -> str:
        """Classify material based on detected item.

        TODO: Replace with a dedicated material classification model
        trained on WasteNet/TACO datasets (Req05).
        Currently uses a simple lookup as placeholder.
        """
        material_map = {
            "bottle": "PET plastic",
            "cup": "paper/plastic composite",
            "bowl": "ceramic",
            "banana": "organic",
            "apple": "organic",
            "sandwich": "organic",
            "cell phone": "e-waste",
            "laptop": "e-waste",
            "remote": "e-waste",
            "book": "paper",
            "scissors": "metal",
            "knife": "metal",
            "spoon": "metal",
            "fork": "metal",
        }
        return material_map.get(item_name, "unknown")
