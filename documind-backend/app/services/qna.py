from app.services.llm import client
import os

MODEL_NAME = os.getenv('GROQ_MODEL')

def generate_questions_and_answers(text: str) -> dict:
    if len(text) > 4000:
        raise ValueError("Text too long, please chunk input")

    response = client.chat.completions.create(
        model=MODEL_NAME,
        temperature=0.3,
        messages=[
            {
                "role": "system",
                "content": (
                    "You are an AI tutor that generates study questions and answers. "
                    "You must return ONLY valid JSON. "
                    "Do not include explanations, markdown, or extra text."
                )
            },
            {
                "role": "user",
                "content": (
                    "From the text below, generate exactly 10 question-and-answer pairs.\n\n"
                    "Rules:\n"
                    "- Questions must be based strictly on the text\n"
                    "- Answers must be 1–2 sentences\n\n"
                    "Return JSON in the following format:\n"
                    "{\n"
                    '  "questions": ["Q1", "Q2", "..."],\n'
                    '  "answers": ["A1", "A2", "..."]\n'
                    "}\n\n"
                    "Text:\n"
                    f"{text}"
                )
            }
        ]
    )

    return response.choices[0].message.content