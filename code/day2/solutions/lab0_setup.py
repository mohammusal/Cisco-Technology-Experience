# Lab 0: Your Webex token - solution

name = "Ola"
print(f"{name} will never share a Webex token in a chat, a screenshot, or GitHub.")
print("The token lives only in token.txt, on this laptop.")

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from config import access_token

token = access_token()
print("Token loaded. It starts with:", token[:6] + "...")
print("Length:", len(token), "characters")
