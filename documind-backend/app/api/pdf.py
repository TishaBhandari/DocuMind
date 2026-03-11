from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.concurrency import run_in_threadpool
import uuid
import json
from pathlib import Path

from app.services.pdf_extractor import extract_text_from_pdf
from app.services.summarizer import summarize_document
from app.services.qna import generate_questions_and_answers

router = APIRouter()

BASE_STORAGE = Path("storage")
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB

PDF_DIR = BASE_STORAGE / "pdfs"
TEXT_DIR = BASE_STORAGE / "extracted"

PDF_DIR.mkdir(parents=True, exist_ok=True)
TEXT_DIR.mkdir(parents=True, exist_ok=True)


@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code=400, detail="Only PDF files are allowed")

    content = await file.read()

    if len(content) > MAX_FILE_SIZE:
        raise HTTPException(status_code=413, detail="File too large")

    pdf_id = str(uuid.uuid4())
    pdf_path = PDF_DIR / f"{pdf_id}.pdf"

    with open(pdf_path, "wb") as f:
        f.write(content)

    # Blocking operation → keep sync here (acceptable)
    text = extract_text_from_pdf(str(pdf_path))

    text_path = TEXT_DIR / f"{pdf_id}.txt"
    text_path.write_text(text, encoding="utf-8")

    return {"pdf_id": pdf_id}


@router.post("/summarize/{pdf_id}")
async def summarize_pdf(pdf_id: str):
    text_path = TEXT_DIR / f"{pdf_id}.txt"

    if not text_path.exists():
        raise HTTPException(status_code=404, detail="PDF not found")

    text = text_path.read_text(encoding="utf-8")

    summary = await run_in_threadpool(summarize_document, text)

    return {"summary": summary}


@router.post("/questions/{pdf_id}")
async def generate_pdf_questions(pdf_id: str):
    text_path = TEXT_DIR / f"{pdf_id}.txt"

    if not text_path.exists():
        raise HTTPException(status_code=404, detail="PDF not found")

    text = text_path.read_text(encoding="utf-8")

    qna = await run_in_threadpool(generate_questions_and_answers, text)

    try:
        parsed = json.loads(qna)
    except json.JSONDecodeError:
        raise ValueError("Model returned invalid JSON")

    return {
        "questions": parsed["questions"],
        "answers": parsed["answers"]
    }