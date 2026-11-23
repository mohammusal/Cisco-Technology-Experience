"""Read the Webex token from token.txt. Never put the token in your script."""

from pathlib import Path

TOKEN_PATH = Path(__file__).resolve().parent / "token.txt"
PLACEHOLDER = "PASTE_YOUR_TOKEN_HERE"


def access_token():
    if not TOKEN_PATH.exists():
        raise SystemExit(
            "No token.txt yet.\n"
            "1. Copy token.example.txt to token.txt\n"
            "2. Paste your personal access token on the first line\n"
            "3. Save, then run this file again"
        )
    token = TOKEN_PATH.read_text(encoding="utf-8").strip().splitlines()[0].strip()
    if not token or token == PLACEHOLDER:
        raise SystemExit(
            "token.txt is empty. Paste your token, save, and run again."
        )
    return token
