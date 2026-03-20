"""Disposal Service — SE + AI component.

Combines a structured recycling rules knowledge base (SE)
with LLM-generated human-friendly instructions (AI).
Location-aware: rules differ by country/region.
"""

import json
import os

KNOWLEDGE_DIR = os.path.join(os.path.dirname(__file__), "..", "knowledge")


class DisposalService:
    def __init__(self):
        self._rules = self._load_rules()

    def _load_rules(self) -> dict:
        """Load recycling rules from the knowledge base."""
        rules_path = os.path.join(KNOWLEDGE_DIR, "recycling_rules.json")
        if os.path.exists(rules_path):
            with open(rules_path) as f:
                return json.load(f)
        return {}

    def get_instructions(
        self,
        item_name: str,
        material: str,
        country: str,
        region: str | None = None,
    ) -> dict:
        """Get location-specific disposal instructions.

        1. Look up rules from the knowledge base (SE — deterministic)
        2. If no exact match, fall back to LLM generation (AI)
        3. Return structured response with category, steps, and env impact
        """
        # Try structured rules first
        country_rules = self._rules.get(country, {})
        category = self._get_disposal_category(material, country_rules)
        steps = self._get_disposal_steps(material, country_rules)

        # If rules are incomplete, use LLM to generate instructions
        if not steps:
            steps = self._generate_instructions_with_llm(
                item_name, material, country, region
            )

        return {
            "item_name": item_name,
            "material": material,
            "country": country,
            "region": region,
            "disposal_category": category,
            "steps": steps,
            "environmental_impact": self._get_environmental_impact(material),
        }

    def _get_disposal_category(self, material: str, country_rules: dict) -> str:
        """Map material to disposal category using rules."""
        category_map = country_rules.get("categories", {})
        if material in category_map:
            return category_map[material]
        # Default fallback
        defaults = {
            "PET plastic": "recyclable",
            "HDPE plastic": "recyclable",
            "glass": "recyclable",
            "aluminum": "recyclable",
            "paper": "recyclable",
            "organic": "compostable",
            "e-waste": "special disposal",
            "metal": "recyclable",
        }
        return defaults.get(material, "landfill")

    def _get_disposal_steps(self, material: str, country_rules: dict) -> list[str]:
        """Get preparation steps from knowledge base."""
        steps = country_rules.get("steps", {})
        return steps.get(material, [])

    def _generate_instructions_with_llm(
        self, item_name: str, material: str, country: str, region: str | None
    ) -> list[str]:
        """Fall back to LLM for generating disposal instructions."""
        try:
            import ollama

            location = f"{region}, {country}" if region else country
            response = ollama.chat(
                model="llama3",
                messages=[{
                    "role": "user",
                    "content": (
                        f"Give 3-5 short disposal steps for a {item_name} "
                        f"(material: {material}) in {location}. "
                        f"Include any location-specific rules like bin colors "
                        f"or special requirements. Be concise, one line per step."
                    ),
                }],
            )
            text = response["message"]["content"]
            return [line.strip("- •0123456789.") .strip() for line in text.strip().split("\n") if line.strip()]
        except Exception:
            return [f"Dispose of {item_name} ({material}) according to local {country} recycling guidelines."]

    def _get_environmental_impact(self, material: str) -> str:
        """Return environmental impact fact for motivation."""
        impacts = {
            "PET plastic": "Recycling one PET bottle saves enough energy to power a lightbulb for 6 hours.",
            "aluminum": "Recycling one aluminum can saves enough energy to power a laptop for 4 hours.",
            "glass": "Recycled glass reduces air pollution by 20% and water pollution by 50%.",
            "paper": "Recycling 1 ton of paper saves 17 trees and 7,000 gallons of water.",
            "organic": "Composting organic waste reduces methane emissions from landfills.",
            "e-waste": "Proper e-waste recycling recovers valuable metals and prevents toxic contamination.",
        }
        return impacts.get(material, "Every item correctly sorted helps reduce landfill waste.")
