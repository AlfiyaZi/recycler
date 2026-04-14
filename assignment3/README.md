# Assignment 3 - Use Cases, Traceability, and Domain Model

**Course:** KV Engineering of AI-intensive Systems

**Project:** Recycling Object Detector

**Team:** Patrik Palencar (AI), Jonatan Schmidlechner (CS), Alfiia Ziganshina (AI MSc)

**Due:** Wednesday, April 15, 2026, 23:59

## Files

| File | Part | Description |
|------|------|-------------|
| `Assignment3_ROD.xlsx` | Part 1 + Part 2 | Use Cases with scenarios + Traceability Matrix |
| `use_case_diagram.drawio` | Part 3 | Use Case Diagram (open in draw.io, export as PDF) |
| `domain_model.drawio` | Part 4 | Domain Model Diagram (open in draw.io, export as PDF) |

## Part 1: Use Cases

### 5 Main Use Cases

| ID | Name | Actors |
|----|------|--------|
| UC1 | Scan Waste Item | User, YOLO Detection Model |
| UC2 | Get Disposal Instructions | User, LLM |
| UC3 | Ask Follow-up Question | User, LLM |
| UC4 | View Scan History | User |
| UC5 | Set Location | User, GPS Service |

### 5 Supporting Use Cases

| ID | Name | Included in | AI-specific |
|----|------|-------------|-------------|
| SUC1 | Detect Object in Image | UC1 | Yes |
| SUC2 | Classify Material | UC1 | Yes |
| SUC3 | Generate LLM Response | UC2, UC3 | Yes |
| SUC4 | Determine User Location | UC2, UC5 | No |
| SUC5 | Validate Image | UC1 | No |

Each UC has: 1 main success scenario + at least 1 alternative + at least 1 exception scenario.

### Actors

| Actor | Type |
|-------|------|
| User | Human (primary) |
| YOLO Detection Model | AI |
| LLM | AI |
| GPS Service | System |

## Part 2: Traceability Matrix

All 22 functional requirements (Req01-Req22) and 19 non-functional requirements (NfReq01-NfReq19) from Assignment 2 are mapped to at least one UC. All UCs (including supporting) are traced to at least one requirement.

| | UC1 | UC2 | UC3 | UC4 | UC5 | SUC1 | SUC2 | SUC3 | SUC4 | SUC5 |
|---|---|---|---|---|---|---|---|---|---|---|
| **Req01** | ✓ | | | | | | | | | |
| **Req02** | ✓ | | | | | | | | | |
| **Req03** | ✓ | | | | | | | | | |
| **Req04** | ✓ | | | | | ✓ | | | | |
| **Req05** | ✓ | | | | | | ✓ | | | |
| **Req06** | ✓ | | | | | ✓ | | | | |
| **Req07** | ✓ | | | | | ✓ | | | | |
| **Req08** | | ✓ | | | | | | | | |
| **Req09** | | ✓ | | | | | | | | |
| **Req10** | | ✓ | | | | | | | | |
| **Req11** | | | ✓ | | | | | | | |
| **Req12** | | | ✓ | | | | | ✓ | | |
| **Req13** | ✓ | | | | | | | | | |
| **Req14** | | | | | ✓ | | | | ✓ | |
| **Req15** | | ✓ | | | | | | | | |
| **Req16** | | | | | ✓ | | | | | |
| **Req17** | | ✓ | | | | | | ✓ | | |
| **Req18** | | | | ✓ | | | | | | |
| **Req19** | | | | ✓ | | | | | | |
| **Req20** | ✓ | | | | | | | | | |
| **Req21** | ✓ | | | | | | | | | ✓ |
| **Req22** | | | | | ✓ | | | | ✓ | |
| **NfReq01** | ✓ | ✓ | ✓ | ✓ | ✓ | | | | | |
| **NfReq02** | ✓ | ✓ | ✓ | ✓ | ✓ | | | | | |
| **NfReq03** | ✓ | | | | | | | | | |
| **NfReq04** | ✓ | | | | | ✓ | ✓ | | | |
| **NfReq05** | | | ✓ | | | | | ✓ | | |
| **NfReq06** | ✓ | ✓ | ✓ | ✓ | ✓ | | | | | |
| **NfReq07** | ✓ | | | | | ✓ | | | | |
| **NfReq08** | | | | | | | ✓ | | | |
| **NfReq09** | ✓ | ✓ | ✓ | ✓ | ✓ | | | | | |
| **NfReq10** | ✓ | | | | | | | | | ✓ |
| **NfReq11** | ✓ | ✓ | ✓ | ✓ | ✓ | | | | | |
| **NfReq12** | ✓ | ✓ | ✓ | | | | | | | |
| **NfReq13** | | | | | | ✓ | ✓ | ✓ | | |
| **NfReq14** | ✓ | | | ✓ | | | | | | |
| **NfReq15** | | | | | | ✓ | ✓ | ✓ | | |
| **NfReq16** | | | | | | ✓ | ✓ | | | |
| **NfReq17** | ✓ | | | | | ✓ | | | | |
| **NfReq18** | ✓ | ✓ | ✓ | | | | | | | |
| **NfReq19** | | | | | | ✓ | ✓ | ✓ | | |

## Part 3: Use Case Diagram

- All UCs and actors shown
- Supporting UCs connected via `<<include>>`
- AI-specific elements highlighted in **blue**
- Open `use_case_diagram.drawio` in [draw.io](https://www.drawio.com/) and export as PDF

## Part 4: Domain Model

11 domain concepts with named relationships and cardinality:

- **User**, **Image**, **WasteItem**, **Material**, **DisposalCategory** (enum)
- **DisposalInstruction**, **Location**, **RecyclingRulesKB**, **ScanRecord**, **ChatMessage**
- **YOLODetectionModel** (AI), **LLM** (AI)

AI-related elements highlighted in **blue**. Open `domain_model.drawio` in [draw.io](https://www.drawio.com/) and export as PDF.

## Before Submitting

1. Open `.drawio` files in draw.io, adjust layout if needed, export as PDF
2. Review Excel in Google Sheets / Excel, tweak wording if needed
3. Submit: Excel + diagram PDFs (one team member submits)
