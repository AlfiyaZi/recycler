from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import detection, disposal, chat

app = FastAPI(
    title="Recycling Object Detector",
    description="AI-powered waste sorting assistant",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # TODO: restrict in production
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(detection.router, prefix="/api/detect", tags=["detection"])
app.include_router(disposal.router, prefix="/api/disposal", tags=["disposal"])
app.include_router(chat.router, prefix="/api/chat", tags=["chat"])


@app.get("/health")
def health_check():
    return {"status": "ok"}
