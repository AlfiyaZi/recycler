# Recycling Object Detector

## Assignment 2 - Requirements Engineering

**Team members:**

Patrik Palenčár (AI student), Jonatan Schmidlechner (Computer Science student), Alfiia Ziganshina (AI MSc)


## Part 1: Goals of the System

### Non-AI Goals
- G1: Make recycling easier and more accessible for people by providing instant waste sorting guidance
- G2: Allow users to capture photos of waste items using their device camera or by uploading an image
- G3: Display recycling instructions in a clear, readable format with category labels and disposal steps
- G4: Maintain a history of previously scanned items so users can review past results
- G5: Support multiple languages for recycling instructions (at minimum English and German)
- G6: Provide country- and region-specific recycling rules so that users traveling or relocating abroad can understand local waste disposal practices (e.g., color-coded bin systems in Austria vs. Germany, or mandatory paid waste bags in South Korea)
- G7: Provide environmental impact information for each recycling action (e.g., CO2 saved, water saved) to increase recycling in general

### AI-Related Goals
- G8: Automatically detect and identify the type of waste item from a photo using object detection and classification (e.g., plastic bottle, glass jar, battery, cardboard box)
  - **Why AI is needed:** The variety of everyday waste items is enormous and constantly changing (new packaging designs, brands, materials). Writing explicit rules for each item is infeasible. A Computer Vision model can generalize across visual variations and process images in real time.
- G9: Classify the material composition of the identified item (e.g., PET plastic, HDPE plastic, aluminum, glass, paper, composite, organic, e-waste)
  - **Why AI is needed:** Material identification from visual appearance alone requires pattern recognition beyond simple color/shape rules. Different plastics look similar but require different recycling streams. An image classifier trained on waste datasets can learn these subtle visual differences.
- G10: Generate human-friendly, location-aware disposal instructions based on the identified item, material, and the user's current country or region
  - **Why AI is needed:** Recycling rules differ drastically between countries (e.g., Austria uses color-coded bins differently than Germany; South Korea requires purchasing designated waste bags). An LLM can combine item context with location-specific recycling knowledge and handle follow-up questions in natural language (e.g., "Where do I buy waste bags in Seoul?" or "What if the bottle still has the label on?").


## Part 2: Stakeholders

### Users
- **General public / Households:** Anyone with a smartphone who is aware of recycling but unsure about how to sort specific items correctly
- **Students and young adults:** Environmentally conscious users, often living on their own for the first time and unfamiliar with local recycling rules
- **Travelers and expats:** People visiting or relocating to a new country who are unfamiliar with local waste disposal systems (e.g., different bin colors, mandatory paid waste bags, deposit-return schemes)
- **Office workers / Facility managers:** People responsible for waste sorting in shared spaces (offices, dormitories, co-working spaces)

### People Affected by the System
- **Waste management workers:** Improved sorting quality reduces contamination in recycling streams, making their work safer and more efficient
- **Recycling facility operators:** Better upstream sorting leads to higher quality recyclable materials and less rejected waste
- **Local communities:** Reduced landfill waste and improved recycling rates benefit the environment for everyone in the area

### Managers
- **Course instructors** (in the context of this course project)
- **Product owner / Development team:** If deployed as a real product, they would manage feature priorities and quality
- **Municipal waste management departments:** Potential partners who define recycling rules and could adopt the system

### Regulators
- **Environmental protection agencies:** Ensure waste management practices comply with local regulations
- **EU regulatory bodies:** The EU AI Act applies since the system uses AI for classification; it would likely fall under minimal risk category
- **Data protection authorities (GDPR):** If photos are stored or processed on a server, user data privacy must be ensured


## Part 3: Functional Requirements (EARS Template)

### Image Capture and Input
- **Req01:** The Recycling Object Detector shall allow users to capture a photo of a waste item using the device camera.
- **Req02:** The Recycling Object Detector shall allow users to upload an existing image from their device gallery.
- **Req03:** When an image is provided, the Recycling Object Detector shall display a loading indicator while processing the image.

### Item Recognition (AI)
- **Req04:** When an image is provided, the Recycling Object Detector shall identify the waste item depicted in the photo and display its name. [AI]
- **Req05:** When an image is provided, the Recycling Object Detector shall classify the material composition of the identified item (e.g., PET plastic, glass, aluminum, paper, organic, e-waste). [AI]
- **Req06:** When an image contains multiple items, the Recycling Object Detector shall detect and classify each item separately. [AI]
- **Req07:** If the system cannot identify the item with sufficient confidence, the Recycling Object Detector shall inform the user that the item could not be recognized and suggest taking a clearer photo.

### Disposal Instructions
- **Req08:** When an item is identified, the Recycling Object Detector shall display the disposal category (recyclable, compostable, landfill, special disposal). [AI]
- **Req09:** When an item is identified, the Recycling Object Detector shall provide step-by-step preparation instructions (e.g., "Rinse the container and remove the cap before recycling").
- **Req10:** When an item is identified, the Recycling Object Detector shall display the environmental impact of correctly recycling the item (e.g., "Recycling this can saves enough energy to power a laptop for 4 hours").

### Follow-up Interaction (AI)
- **Req11:** The Recycling Object Detector shall allow users to ask follow-up questions in natural language about the scanned item (e.g., "Can I recycle this if it is greasy?"). [AI]
- **Req12:** When a follow-up question is asked, the Recycling Object Detector shall generate a relevant answer based on the identified item context. [AI]

### Live Camera Detection (AI)
- **Req13:** While the camera is open, the Recycling Object Detector shall continuously process the camera feed to detect and highlight waste items in real time. [AI]

### Location-Aware Recycling Rules
- **Req14:** The Recycling Object Detector shall allow users to select their country and region or use GPS-based location detection to determine local recycling rules.
- **Req15:** When an item is identified, the Recycling Object Detector shall provide disposal instructions specific to the user's selected location (e.g., which bin color to use, whether a deposit-return system applies, or whether special waste bags must be purchased).
- **Req16:** When the user changes their location, the Recycling Object Detector shall update all disposal instructions to reflect the new region's rules.
- **Req17:** If the user's language differs from the location's default language when disposal instructions are generated, the Recycling Object Detector shall display instructions in the user's preferred language. [AI]

### History and User Features
- **Req18:** The Recycling Object Detector shall store a history of previously scanned items with their classification results.
- **Req19:** When the user opens the history, the Recycling Object Detector shall display a list of past scans with item name, category, and date.

### Error Handling
- **Req20:** If the camera is not available, the Recycling Object Detector shall prompt the user to upload an image instead.
- **Req21:** If the uploaded image does not contain a recognizable object, the Recycling Object Detector shall display a message asking the user to try a different image.
- **Req22:** If the user's location is not set or cannot be determined, the Recycling Object Detector shall prompt the user to manually select their country and region before providing disposal instructions.


## Part 4: Non-Functional Requirements (EARS Template)

### External Interfaces
- **NfReq01:** The Recycling Object Detector shall provide a web-based user interface accessible from modern browsers (Chrome, Firefox, Safari, Edge). [External Interface]
- **NfReq02:** The Recycling Object Detector shall also be usable as a mobile-responsive web application on iOS and Android devices. [External Interface]
- **NfReq03:** The Recycling Object Detector shall integrate with the device camera API for real-time photo capture. [External Interface]

### Performance
- **NfReq04:** When an image is submitted, the image classification shall produce results in less than 3 seconds. [Performance] [AI]
- **NfReq05:** When a follow-up question is asked, the LLM shall generate a response in less than 5 seconds. [Performance] [AI]
- **NfReq06:** The Recycling Object Detector shall support at least 50 concurrent users without performance degradation. [Performance]

### Attributes
- **NfReq07:** The image classification model shall achieve at least 80% top-1 accuracy on the waste item identification task. [Attributes] [AI]
- **NfReq08:** The material classification model shall achieve at least 75% accuracy across all material categories. [Attributes] [AI]
- **NfReq09:** The Recycling Object Detector shall be available at least 99% of the time during normal operation. [Attributes]
- **NfReq10:** The Recycling Object Detector shall store no personally identifiable information from uploaded images; images shall be processed and discarded unless the user explicitly saves them to history. [Attributes]
- **NfReq11:** The Recycling Object Detector user interface shall be usable by users with no technical background, requiring no training to operate. [Attributes]

### Constraints
- **NfReq12:** The Recycling Object Detector shall be developed using Python for the backend and a standard web framework for the frontend. [Constraint]
- **NfReq13:** The AI models shall run on commodity hardware (no GPU requirement for inference) or use a free-tier cloud API. [Constraint]
- **NfReq14:** The Recycling Object Detector shall comply with GDPR requirements for any data processing involving user images. [Constraint]
- **NfReq15:** The Recycling Object Detector shall use open-source or freely available pre-trained models (e.g., from HuggingFace) to avoid licensing costs. [Constraint]

### AI-Specific Quality
- **NfReq16:** The classification model shall not produce systematically different accuracy rates across waste items from different cultural or regional origins. [Attributes] [AI]
- **NfReq17:** When displaying results, the Recycling Object Detector shall show the confidence score and the top-3 possible classifications. [Attributes] [AI]
- **NfReq18:** The Recycling Object Detector shall clearly indicate that classifications are AI-generated and may contain errors. [Attributes] [AI]
- **NfReq19:** The AI models used shall be open-source, and their training data sources shall be documented. [Constraint] [AI]


## Part 5: AI-Related Requirements

### Functional AI Requirements

| ID | Requirement | Threshold | Justification | Implementation Plan |
|----|-------------|-----------|---------------|---------------------|
| Req04 | Item identification from photo | Top-1 accuracy >= 80% | Users need reliable identification; below 80% the system becomes frustrating and untrustworthy. 80% is achievable with transfer learning on waste datasets. | Fine-tune a pre-trained YOLO or CLIP model on the TrashNet dataset (~2500 images, 6 categories) augmented with additional waste images from Kaggle. Use transfer learning to keep training costs low. |
| Req05 | Material classification | Accuracy >= 75% | Material identification is harder than item detection (e.g., distinguishing PET from HDPE plastic). 75% is realistic for visual-only classification. | Train a secondary classifier on top of the object detection features. Use datasets like WasteNet or TACO. Consider multi-label classification for composite items. |
| Req06 | Multi-item detection | Detect >= 90% of items when 2-5 items are in frame | Users may photograph a pile of items at once. | Use YOLO's built-in multi-object detection with confidence threshold tuning. |
| Req08 | Disposal category classification | Accuracy >= 85% | Mapping items to disposal categories (recyclable/compostable/landfill/special) is simpler than material identification since there are fewer categories. | Rule-based mapping from material classification to disposal categories, combined with LLM fallback for edge cases. |
| Req11-12 | Natural language follow-up Q&A | Relevant response in >= 90% of cases | Users expect helpful answers; irrelevant responses erode trust. | Use Ollama to run a local LLM (e.g., Llama 3 or Mistral) with few-shot prompting. Provide item context, user location, and recycling knowledge as prompt context. |
| Req13 | Real-time camera detection | Detection at >= 10 FPS on mobile device | Users expect smooth real-time feedback when pointing the camera at items. Below 10 FPS feels laggy and unusable. | Use a lightweight YOLO variant (YOLOv8n) optimized for mobile inference. Consider ONNX export for cross-platform performance. |
| Req15 | Location-specific disposal instructions | Correct location-specific advice in >= 85% of supported countries | Incorrect local instructions (e.g., wrong bin color) lead to contamination or fines. Rules differ drastically between countries. | Maintain a structured knowledge base of recycling rules per country/region. Feed location context into the LLM prompt so that disposal instructions are tailored to the user's current location. |
| Req17 | Cross-language instruction generation | Correct translation in >= 90% of cases for supported languages | Travelers need instructions in their own language, not the local language. Poor translations lead to confusion. | Use the LLM's multilingual capabilities to generate instructions in the user's preferred language while incorporating location-specific rules. |

### Non-Functional AI Requirements

| ID | Requirement | AI-Specific Category | Details |
|----|-------------|---------------------|---------|
| NfReq04 | Classification in < 3 seconds | **Performance / Safety** | Slow responses make the app unusable in real-time scenarios (e.g., standing at a recycling bin). Using a lightweight model (MobileNet, EfficientNet-Lite) ensures fast inference even on CPU. |
| NfReq07-08 | Accuracy thresholds (80% / 75%) | **Safety** | Incorrect classification leads to contaminated recycling streams or recyclable items going to landfill. The system should display a confidence score and warn users when confidence is low. |
| NfReq10 | No PII storage from images | **Security and Privacy** | Photos may contain faces, addresses, or other personal information in the background. Images must be processed ephemerally and never stored without explicit consent. GDPR compliance is mandatory. |
| NfReq16 | The classification model shall not produce systematically different accuracy rates across waste items from different cultural or regional origins | **Fairness** | Waste packaging varies significantly across countries and cultures. The training dataset must include diverse packaging from multiple regions to avoid bias toward Western brands only. |
| NfReq17 | When displaying results, the Recycling Object Detector shall show the confidence score and the top-3 possible classifications | **Explainability** | Users should understand why the system made a particular classification. Showing alternatives and confidence helps users make informed decisions and builds trust. |
| NfReq18 | The Recycling Object Detector shall clearly indicate that classifications are AI-generated and may contain errors | **Transparency and Trust** | Users must know they are interacting with an AI system. A disclaimer prevents over-reliance on potentially incorrect classifications. |
| NfReq19 | The AI models used shall be open-source, and their training data sources shall be documented | **Ethics, Regulation, Organizational Culture** | Using open-source models ensures reproducibility and auditability. Documenting training data sources is good practice under the EU AI Act and supports academic integrity. |
