import os
from pathlib import Path
from dotenv import load_dotenv
from google import genai

# Load env
BASE_DIR = Path(__file__).resolve().parent
ENV_PATH = BASE_DIR / ".env"
load_dotenv(dotenv_path=ENV_PATH, override=True)

api_key = os.getenv("GEMINI_API_KEY")
print("KEY LOADED:", api_key is not None)

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model="models/gemini-flash-latest",
    contents="Say hello in one word"
)

print("RESPONSE:", response.text)
