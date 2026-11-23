# Checkpoint after Lab 2: room + welcome + details file

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from config import access_token

from webexteamssdk import WebexTeamsAPI

api = WebexTeamsAPI(access_token=access_token())

title = "Krakow CTE Group 1"
room = api.rooms.create(title=title)
print("Created:", room.title)
print("Room ID:", room.id)

api.messages.create(
    roomId=room.id,
    text="Welcome! Your room has been created!",
)

Path("room_details.txt").write_text(
    f"Room Title: {room.title}\nRoom ID: {room.id}\n",
    encoding="utf-8",
)
print("Wrote room_details.txt")
