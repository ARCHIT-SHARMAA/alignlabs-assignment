import os
import json
from google import genai
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise RuntimeError("GEMINI_API_KEY not set")

client = genai.Client(api_key=GEMINI_API_KEY)

MODEL_NAME = "models/gemini-flash-latest"


def generate_structured_output(scraped_data: dict) -> dict:
    """
    Takes scraped website data and returns structured JSON.
    If Gemini quota is exhausted, falls back to rule-based structure.
    """

    prompt = f"""
You are an information extraction system.

From the following website content, return ONLY valid JSON with this schema:

{{
  "company_name": string,
  "website": string,
  "summary": string,
  "emails": [],
  "phone_numbers": [],
  "socials": [],
  "addresses": [],
  "notes": "",
  "sources": []
}}

Website data:
{json.dumps(scraped_data)}
"""

    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt
        )

        text = response.text.strip()

        # Ensure JSON only
        start = text.find("{")
        end = text.rfind("}") + 1
        json_text = text[start:end]

        return json.loads(json_text)

    except Exception as e:
        # ✅ SAFE FALLBACK (important for assignment)
        return {
            "company_name": scraped_data.get("company", "Unknown"),
            "website": scraped_data.get("website"),
            "summary": "Structured summary unavailable due to LLM quota limits.",
            "emails": scraped_data.get("emails", []),
            "phone_numbers": scraped_data.get("phone_numbers", []),
            "socials": scraped_data.get("socials", []),
            "addresses": [],
            "notes": str(e),
            "sources": scraped_data.get("pages", [])
        }
