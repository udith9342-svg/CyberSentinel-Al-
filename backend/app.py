"""FastAPI entry point for CyberSentinel AI prototype."""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from agent import analyze_sample

app = FastAPI(title="CyberSentinel AI", version="0.1.0")

# Development-only CORS so the static frontend can call localhost.
# Restrict origins before deploying this application.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

class AnalysisRequest(BaseModel):
    input_type: str
    text: str

@app.get("/")
def health():
    return {"status": "running", "project": "CyberSentinel AI"}

@app.post("/analyze")
def analyze(request: AnalysisRequest):
    return analyze_sample(request.input_type, request.text)
