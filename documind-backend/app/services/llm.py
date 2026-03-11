from openai import OpenAI
from app.core.config import GROQ_API_KEY, GROQ_BASE_URL

client = OpenAI(
    base_url=GROQ_BASE_URL,
    api_key=GROQ_API_KEY
)