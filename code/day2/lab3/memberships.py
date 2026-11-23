# Lab 3: Add people to the room
# Put your room id in room_id.txt (Lab 2 wrote it inside room_details.txt).

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from config import access_token

from webexteamssdk import WebexTeamsAPI

api = WebexTeamsAPI(access_token=access_token())

# TODO 1: Paste the Room ID from room_details.txt between the quotes.
room_id = "PASTE_ROOM_ID_HERE"

# TODO 2: Put your group members' emails here. Keep your own email out:
# you are already in the room because you created it.
members = [
    "ola@example.com",
    "jan@example.com",
]

# TODO 3: Remove the # to add each person as a moderator and welcome them.
# for email in members:
#     membership = api.memberships.create(
#         roomId=room_id,
#         personEmail=email,
#         isModerator=True,
#     )
#     api.messages.create(
#         roomId=room_id,
#         markdown=f"Welcome onboard, <@{membership.personId}>",
#     )
#     print("Added:", email)

# TODO 4: List who is in the room now.
# print("\nPeople in the room:")
# for member in api.memberships.list(roomId=room_id):
#     print("-", member.personDisplayName, member.personEmail)
