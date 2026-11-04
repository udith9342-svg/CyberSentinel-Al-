"""Coordinator for detection modules. Replace the placeholder with verified analysis logic."""
from detectors.email_detector import inspect_email
from detectors.url_checker import inspect_url
from detectors.message_detector import inspect_message

def analyze_sample(input_type: str, text: str):
    kind = input_type.lower().strip()
    if not text.strip():
        return {"status": "needs_input", "message": "No content was provided."}
    if kind == "email":
        findings = inspect_email(text)
    elif kind == "url":
        findings = inspect_url(text)
    elif kind == "message":
        findings = inspect_message(text)
    else:
        return {"status": "planned", "message": f"The {kind} detector is planned and is not implemented yet."}
    return {"status": "prototype", "message": "Rule-based prototype checks only; not a verified security verdict.", "findings": findings}
