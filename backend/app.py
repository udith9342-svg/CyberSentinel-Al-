"""FastAPI entry point for CyberSentinel AI. Detection logic is intentionally not claimed as implemented yet."""
from fastapi import FastAPI
from pydantic import BaseModel
from agent import analyze_sample

app = FastAPI(title="CyberSentinel AI", version="0.1.0")

class AnalysisRequest(BaseModel):
    input_type: str
    text: str

@app.get("/")
def health():
    return {"status": "running", "project": "CyberSentinel AI"}

@app.post("/analyze")
def analyze(request: AnalysisRequest):
    return analyze_sample(request.input_type, request.text)
