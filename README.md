# Recycling Object Detector

An AI-powered waste sorting assistant that helps users correctly recycle items by taking a photo.

## Team

- Alfiia Ziganshina (AI MSc)
- Patrik Palenčár (AI)
- Jonatan Schmidlechner (Computer Science)

**Course:** KV Engineering of AI-intensive Systems, JKU Linz

## Overview

Users photograph a waste item → the system identifies it using computer vision, classifies the material, and provides location-specific disposal instructions. Users can ask follow-up questions in natural language.

## Architecture

```
┌─────────────────────────────────────────────────────┐
│                   Frontend (Web/Mobile)              │
│              React · Mobile-responsive               │
│   Camera Capture · Image Upload · Chat Interface     │
└──────────────────────┬──────────────────────────────┘
                       │ REST API
┌──────────────────────▼──────────────────────────────┐
│                   Backend (Python/FastAPI)            │
│                                                      │
│  ┌─────────────┐  ┌──────────────┐  ┌────────────┐  │
│  │  Detection   │  │  Disposal    │  │  Chat /    │  │
│  │  Service     │  │  Service     │  │  Q&A       │  │
│  │             │  │              │  │  Service   │  │
│  │  YOLO model │  │  Rules DB +  │  │  LLM via   │  │
│  │  Object ID  │  │  Location    │  │  Ollama    │  │
│  │  Material   │  │  awareness   │  │            │  │
│  └─────────────┘  └──────────────┘  └────────────┘  │
│       [AI]              [SE+AI]          [AI]        │
└─────────────────────────────────────────────────────┘
```

### How SE + AI Work Together

| Layer | Software Engineering | AI Component |
|-------|---------------------|-------------|
| **Frontend** | React UI, camera API, responsive design, error handling | — |
| **API** | FastAPI routes, validation, auth, rate limiting | — |
| **Detection Service** | Image preprocessing, confidence thresholds, error handling | YOLO object detection + material classification |
| **Disposal Service** | Location rules database, structured knowledge base, caching | LLM generates human-friendly instructions from rules + item context |
| **Chat Service** | Session management, prompt engineering, response validation | LLM for natural language follow-up Q&A |
| **Infrastructure** | Docker, CI/CD, monitoring, logging, GDPR compliance | Model versioning, A/B testing, accuracy monitoring |

## Tech Stack

- **Backend:** Python, FastAPI
- **Frontend:** React (mobile-responsive PWA)
- **AI Models:** YOLOv8 (object detection), fine-tuned classifier (material), Ollama + Llama 3 / Mistral (LLM)
- **Data:** TrashNet, TACO, WasteNet datasets + recycling rules knowledge base
- **Deployment:** Docker, commodity hardware (no GPU required for inference)

## Project Structure

```
├── backend/
│   ├── app/
│   │   ├── api/          # FastAPI routes
│   │   ├── models/       # AI model loading & inference
│   │   ├── services/     # Business logic (detection, disposal, chat)
│   │   └── knowledge/    # Location-specific recycling rules
│   ├── tests/
│   └── requirements.txt
├── frontend/
│   └── src/
│       ├── components/   # Reusable UI components
│       ├── pages/        # Camera, Results, History, Chat
│       ├── styles/
│       └── utils/        # API client, location helpers
├── docs/                 # Assignments & documentation
└── README.md
```

## Getting Started

```bash
# Backend
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload

# Frontend
cd frontend
npm install
npm run dev
```

## Requirements

See [docs/Assignment2_Requirements.md](docs/Assignment2_Requirements.md) for full requirements specification.
