# Assignment 1 - Initial Project Idea and Team Members

**Course:** KV Engineering of AI-intensive Systems

**Team Members:**
- Alfiia Ziganshina (AI MSc)
- *(Looking for a CS/SE partner — to be updated)*

---

## Q1. What is the domain of your system?

Environmental sustainability and waste management.

## Q2. Who would be the users of your system?

General public, households, students, and office workers — anyone who is unsure how to properly sort and dispose of everyday waste items.

## Q3. What is the main goal of your system?

To help users correctly identify how to recycle or dispose of everyday items by simply taking a photo. The system aims to reduce contamination in recycling streams and make waste sorting effortless.

## Q4. How would your system achieve its goal?

The user takes a photo of an item (e.g., a plastic bottle, food packaging, electronics, or a battery). The system then:

1. **Identifies the object** and its material composition (e.g., PET plastic, glass, aluminum, paper, composite, organic waste).
2. **Classifies the disposal category** — recyclable, compostable, landfill, or special disposal (e-waste, hazardous).
3. **Provides recycling instructions** tailored to the item, including preparation steps (e.g., "rinse and remove the cap before recycling").
4. **Gives environmental impact context** to motivate the user (e.g., "recycling this aluminum can saves enough energy to power a laptop for 4 hours").

## Q5. Which type of AI/ML strategy would be required/useful and why?

- **Computer Vision (Object Detection):** To detect and identify the item in the photo. A pre-trained model such as YOLO or CLIP can be used for robust object recognition across diverse everyday items.
- **Image Classification:** To categorize the detected object by material type and disposal category. A fine-tuned classifier trained on waste/recycling datasets (e.g., TrashNet or similar) would handle categories such as plastic, glass, metal, paper, cardboard, organic, and e-waste.
- **Natural Language Processing / LLM:** To generate clear, human-friendly disposal instructions and allow the user to ask follow-up questions in natural language (e.g., "Can I recycle a greasy pizza box?" or "Where do I dispose of old batteries?").
