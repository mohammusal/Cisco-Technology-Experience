# Lab 3: Add people to the room - solution

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from config import access_token

from webexteamssdk import WebexTeamsAPI

api = WebexTeamsAPI(access_token=access_token())

room_id = "PASTE_ROOM_ID_HERE"
members = [
    "ola@example.com",
    "jan@example.com",
]

for email in members:
    membership = api.memberships.create(
        roomId=room_id,
        personEmail=email,
        isModerator=True,
    )
    api.messages.create(
        roomId=room_id,
        markdown=f"Welcome onboard, <@{membership.personId}>",
    )
    print("Added:", email)

print("\nPeople in the room:")
for member in api.memberships.list(roomId=room_id):
    print("-", member.personDisplayName, member.personEmail)
