# Checkpoint after Lab 5: full group project (fill in emails, room id, bot)

import sys
from pathlib import Path

import requests

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from config import access_token

from webexteamssdk import WebexTeamsAPI

api = WebexTeamsAPI(access_token=access_token())
token = access_token()
headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json",
}

# --- Lab 2 ---
title = "Krakow CTE Group 1"
room = api.rooms.create(title=title)
print("Created:", room.title, room.id)
api.messages.create(
    roomId=room.id,
    text="Welcome! Your room has been created!",
)
Path("room_details.txt").write_text(
    f"Room Title: {room.title}\nRoom ID: {room.id}\n",
    encoding="utf-8",
)

# --- Lab 3 ---
members = ["ola@example.com", "jan@example.com"]
for email in members:
    membership = api.memberships.create(
        roomId=room.id, personEmail=email, isModerator=True
    )
    api.messages.create(
        roomId=room.id,
        markdown=f"Welcome onboard, <@{membership.personId}>",
    )

# --- Lab 4 ---
message = api.messages.create(
    roomId=room.id,
    text="This is a draft. We will edit it in a moment.",
)
requests.put(
    f"https://webexapis.com/v1/messages/{message.id}",
    headers=headers,
    json={"roomId": room.id, "text": "This message was edited by Python!"},
)
api.messages.delete(message.id)

# --- Lab 5 ---
bot_email = "mybot@webex.bot"
api.memberships.create(roomId=room.id, personEmail=bot_email, isModerator=False)
api.messages.create(
    roomId=room.id,
    text="Hi, I am Ola from Krakow and I like Python.",
)
lines = []
for item in api.messages.list(roomId=room.id):
    lines.append(f"{item.personEmail or 'unknown'}: {item.text or ''}")
Path("messages.txt").write_text("\n".join(lines), encoding="utf-8")
print("Wrote messages.txt")
