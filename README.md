# CyberSentinel AI

**Detect · Analyze · Protect**

CyberSentinel AI is a hackathon prototype concept for inspecting potentially harmful digital content, including phishing emails, suspicious URLs and social-engineering messages. Voice-clone and deepfake-video detection are planned modules.

## Repository layout

- `frontend/` — browser interface (HTML, CSS and JavaScript)
- `backend/app.py` — FastAPI application entry point
- `backend/agent.py` — routes requests to detector modules
- `backend/detectors/` — separate email, URL, message, voice and video modules
- `backend/models/` — reserved for future model assets
- `backend/utils/` — shared helpers and database placeholder
- `backend/requirements.txt` — Python dependencies

## Run the backend

From the repository root:

```bash
cd backend
python -m venv .venv
# Windows: .venv\\Scripts\\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
uvicorn app:app --reload
```

Open `frontend/index.html` in a browser. The frontend expects the API at `http://127.0.0.1:8000`.

## Current implementation status

The UI and basic rule-based illustrative checks are a starting prototype only. They are **not** a trained AI system, verified phishing detector, URL reputation service, voice-clone detector or deepfake detector. Audio/video analysis and database integration are placeholders. Do not rely on this project to make security decisions or submit confidential data.

## Security notes

- Never commit real API keys, passwords, tokens or private user data.
- Keep local secrets in an ignored `.env` file; use `.env.example` for placeholder variable names only.
- Validate uploads and URLs before adding real analysis services.

## License

See [LICENSE](LICENSE).
