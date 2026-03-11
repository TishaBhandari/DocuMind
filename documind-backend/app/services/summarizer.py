import hashlib
from app.services.llm import client
from app.services.cache_service import (
    get_cached_summary,
    store_summary
)
import os

MODEL_NAME = os.getenv("GROQ_MODEL")

def _hash_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

def summarize_document(text: str) -> str:
    if len(text) > 4000:
        raise ValueError("Text too long, please chunk input")

    text_hash = _hash_text(text)

    cached = get_cached_summary(text_hash)
    if cached:
        return cached

    response = client.chat.completions.create(
        model=MODEL_NAME,
        temperature=0.3,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an AI study assistant designed to summarize academic content "
                    "clearly and concisely for undergraduate students."
                )
            },
            {
                "role": "user",
                "content": (
                    "Summarize the following text into concise study notes.\n"
                    "- Use bullet points\n"
                    "- Maximum 5 bullets\n\n"
                    f"Text:\n{text}"
                )
            }
        ]
    )

    summary = response.choices[0].message.content
    store_summary(text_hash, summary, MODEL_NAME)

    return summary