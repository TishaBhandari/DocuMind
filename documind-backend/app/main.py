from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.pdf import router as pdf_router
from app.services.cache_service import init_cache

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

init_cache()

@app.get("/")
def root():
    return "root"

app.include_router(pdf_router, prefix="/api/pdf", tags=["PDF"])