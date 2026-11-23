# Lab 5: Bots, introductions, and a message log - solution

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from config import access_token

from webexteamssdk import WebexTeamsAPI

api = WebexTeamsAPI(access_token=access_token())

room_id = "PASTE_ROOM_ID_HERE"
bot_email = "mybot@webex.bot"

api.memberships.create(roomId=room_id, personEmail=bot_email, isModerator=False)
print("Bot added:", bot_email)

api.messages.create(
    roomId=room_id,
    text="Hi, I am Ola from Krakow and I like Python.",
)
print("Introduction sent. Wait until everyone in the group has done this.")

lines = []
for message in api.messages.list(roomId=room_id):
    who = message.personEmail or "unknown"
    text = message.text or ""
    lines.append(f"{who}: {text}")
Path("messages.txt").write_text("\n".join(lines), encoding="utf-8")
print(f"Wrote {len(lines)} messages to messages.txt")
