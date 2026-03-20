"""Chat Service — AI component.

Handles natural language follow-up questions about scanned items.
Uses a local LLM via Ollama with item and location context.
"""


class ChatService:
    def ask(
        self,
        question: str,
        item_name: str | None = None,
        material: str | None = None,
        country: str | None = None,
    ) -> str:
        """Answer a follow-up question about a waste item."""
        try:
            import ollama

            context_parts = []
            if item_name:
                context_parts.append(f"The user scanned: {item_name}")
            if material:
                context_parts.append(f"Material: {material}")
            if country:
                context_parts.append(f"Location: {country}")
            context = ". ".join(context_parts)

            system_prompt = (
                "You are a helpful recycling assistant. "
                "Answer questions about waste disposal concisely. "
                "If the user's location is known, give location-specific advice. "
                "Always mention if you are unsure."
            )

            response = ollama.chat(
                model="llama3",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": f"{context}\n\nQuestion: {question}"},
                ],
            )
            return response["message"]["content"]
        except Exception:
            return (
                "Sorry, the chat service is currently unavailable. "
                "Please check the disposal instructions on the results page."
            )
