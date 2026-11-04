"""Basic illustrative email checks; not an AI model or production phishing detector."""
def inspect_email(text: str) -> list[str]:
    findings = []
    lowered = text.lower()
    for phrase in ("verify your account", "urgent action", "password expires", "send otp", "click here"):
        if phrase in lowered:
            findings.append(f"Potentially suspicious wording: {phrase}")
    if not findings:
        findings.append("No configured phrase matched. This does not prove the email is safe.")
    return findings
