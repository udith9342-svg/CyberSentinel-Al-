"""Illustrative keyword checks for social-engineering messages."""
def inspect_message(text: str) -> list[str]:
    lowered = text.lower()
    triggers = ("act now", "account blocked", "limited time", "share your otp", "verify immediately", "you won")
    matches = [f"Possible pressure or manipulation phrase: {item}" for item in triggers if item in lowered]
    return matches or ["No configured phrase matched. Context and sender identity are not verified."]
