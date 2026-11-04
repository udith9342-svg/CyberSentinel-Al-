"""Shared helper functions."""
def normalize_text(value: str) -> str:
    return " ".join(value.strip().split())
