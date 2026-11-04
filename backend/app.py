"""FastAPI entry point for the CyberSentinel AI prototype."""
from fastapi import FastAPI, File, Form, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from agent import analyze_sample

app = FastAPI(title="CyberSentinel AI", version="0.1.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Development only; restrict before deployment.
    allow_credentials=False,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

MAX_UPLOAD_BYTES = 20 * 1024 * 1024
ALLOWED_MEDIA = {
    "audio": ("audio/",),
    "video": ("video/",),
}

@app.get("/")
def health():
    return {"status": "running", "project": "CyberSentinel AI"}

@app.post("/analyze")
async def analyze(
    input_type: str = Form(...),
    text: str = Form(""),
    file: UploadFile | None = File(default=None),
):
    kind = input_type.lower().strip()
    if kind not in {"email", "url", "message", "audio", "video"}:
        raise HTTPException(status_code=400, detail="Unsupported input type.")

    if file is not None:
        if kind not in ALLOWED_MEDIA:
            raise HTTPException(status_code=400, detail="File uploads are currently for audio/video only.")
        content_type = file.content_type or ""
        if not content_type.startswith(ALLOWED_MEDIA[kind]):
            raise HTTPException(status_code=415, detail=f"Expected a {kind} file.")
        data = await file.read(MAX_UPLOAD_BYTES + 1)
        if len(data) > MAX_UPLOAD_BYTES:
            raise HTTPException(status_code=413, detail="File exceeds the 20 MB limit.")
        if not data:
            raise HTTPException(status_code=400, detail="The uploaded file is empty.")
        # Do not save uploaded media. Detection is a planned module.
        return {
            "status": "planned",
            "risk_level": "Not analyzed",
            "summary": f"{kind.title()} upload received successfully.",
            "findings": [],
            "recommendation": "The media detector is not implemented yet. No authenticity or deepfake verdict was generated.",
        }

    if kind in {"audio", "video"}:
        raise HTTPException(status_code=400, detail=f"Attach a {kind} file to continue.")
    if not text.strip():
        raise HTTPException(status_code=400, detail="Paste content to analyze.")

    result = analyze_sample(kind, text)
    return {
        "status": result.get("status", "prototype"),
        "risk_level": "Preliminary checks only",
        "summary": result.get("message", "Prototype checks completed."),
        "findings": result.get("findings", []),
        "recommendation": "This is not a verified security verdict. Verify the sender and destination independently.",
    }
