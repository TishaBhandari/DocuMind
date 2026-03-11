#  DocuMind – Smart Study Buddy

DocuMind is a full-stack AI-powered study assistant that allows users to upload PDF documents and generate concise summaries or study-ready questions and answers using Large Language Models.
---

##  Features

- Upload PDF documents
- Extract and persist text from PDFs
- Generate concise study summaries on demand
- Generate structured question–answer pairs for revision
- Cache AI outputs to reduce redundant computation
- Clean, responsive frontend optimized for studying

---

##  Architecture Overview
React (Vite + Bootstrap)
|
| HTTP (Axios)
v
FastAPI Backend
|
| PDF Processing + LLM Inference
v
Filesystem + SQLite Cache

---

##  Key Design Decisions

- Text extraction is done once during upload to avoid repeated computation
- Summarization and Q&A generation are on-demand, not automatic
- SQLite caching is used to prevent redundant LLM calls
- Blocking LLM calls are safely handled using thread pools
- Environment variables are used for API configuration
- Chunking is intentionally scoped out for MVP simplicity

---

##  Tech Stack

### Frontend
- React (Vite)
- Bootstrap 5
- Axios
- Plain CSS

### Backend
- FastAPI
- Uvicorn
- PyMuPDF (PDF text extraction)
- OpenAI-compatible Groq API
- SQLite (cache)
- python-dotenv

---

## 🔌 API Endpoints

Base URL: /api/pdf

| Endpoint | Method | Description |
|--------|--------|------------|
| `/upload` | POST | Upload PDF |
| `/summarize/{pdf_id}` | POST | Generate summary |
| `/questions/{pdf_id}` | POST | Generate Q&A |

### Summary Response

```json
{
  "summary": "..."
}
```
### QNA Response
```json
{
  "questions": ["Q1", "Q2", "..."],
  "answers": ["A1", "A2", "..."]
}
```

## Future Improvements

Text chunking for large PDFs

Redis-based caching

Flashcard mode for Q&A

User authentication

PDF preview in frontend

Background job processing
