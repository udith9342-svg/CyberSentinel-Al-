"""Basic URL string checks; does not visit URLs or verify reputation."""
from urllib.parse import urlparse

def inspect_url(value: str) -> list[str]:
    parsed = urlparse(value.strip())
    findings = []
    if parsed.scheme not in ("http", "https") or not parsed.netloc:
        findings.append("Input does not look like a complete HTTP or HTTPS URL.")
    if parsed.scheme == "http":
        findings.append("URL uses HTTP rather than HTTPS.")
    host = parsed.hostname or ""
    if host and ("xn--" in host or host.count(".") >= 4):
        findings.append("Check the hostname carefully for lookalike or unusually nested domains.")
    if not findings:
        findings.append("Basic format checks passed only; domain reputation and page content were not checked.")
    return findings
