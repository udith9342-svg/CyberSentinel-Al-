# CyberSentinel AI

**Detect · Analyze · Protect**

CyberSentinel AI is a hackathon prototype for inspecting potentially harmful digital content: phishing emails, suspicious URLs and social-engineering messages. Audio and video upload paths are connected, but voice-clone and deepfake detection are planned modules.

## One project structure

- `frontend/` — the single web interface (HTML, CSS, JavaScript)
- `backend/app.py` — FastAPI entry point and API endpoint
- `backend/agent.py` — routes text requests to detector modules
- `backend/detectors/` — email, URL, message, voice and video modules
- `backend/models/` — reserved for future model assets
- `backend/utils/` — shared helpers and database placeholder
- `backend/requirements.txt` — Python dependencies

## Run locally (Windows)

Open two VS Code terminals from the repository root.

**Terminal 1 — backend**
```powershell
cd backend
py -m venv .venv
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app:app --reload
```

If PowerShell blocks activation, run `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` in that terminal, then activate again.

**Terminal 2 — frontend**
```powershell
py -m http.server 5500
```

Open `http://127.0.0.1:5500/frontend/` in your browser. Backend health check: `http://127.0.0.1:8000/`. API documentation: `http://127.0.0.1:8000/docs`.

## Current implementation status

The interface and basic keyword/URL-format checks are an early rule-based prototype, not a trained AI system or verified phishing detector. The API accepts audio/video uploads up to 20 MB but does not save or analyze the media; those detectors are placeholders. Database integration is also a placeholder. A clean result does not prove content is safe.

## Safety and development notes

- Never commit real API keys, passwords, tokens, private recordings or confidential user data.
- Keep local secrets in an ignored `.env` file; `.env.example` contains placeholders only.
- The permissive CORS configuration is for local development only and must be restricted before deployment.
- Validate uploads, URLs and external service responses before adding production detection services.

## License

See [LICENSE](LICENSE).
