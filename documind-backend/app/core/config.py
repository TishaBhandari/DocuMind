from dotenv import load_dotenv
import os

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_BASE_URL = os.getenv("GROQ_BASE_URL")


if not GROQ_API_KEY:
    raise RuntimeError("GROQ_API_KEY not set")

if not GROQ_BASE_URL:
    raise RuntimeError("GROQ_BASE_URL not set")
