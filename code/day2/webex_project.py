# Day 2 project: your group's Webex room
# This file grows after Labs 2-5. Copy working pieces from the lab files.

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from config import access_token

from webexteamssdk import WebexTeamsAPI

api = WebexTeamsAPI(access_token=access_token())

# --- Lab 2: create the room and a welcome message ---
title = "Krakow CTE Group 1"
# room = api.rooms.create(title=title)
# print("Created:", room.title, room.id)

# --- Lab 3: add your group ---
# members = ["ola@example.com", "jan@example.com"]
# for email in members:
#     membership = api.memberships.create(
#         roomId=room.id, personEmail=email, isModerator=True
#     )
#     api.messages.create(
#         roomId=room.id,
#         markdown=f"Welcome onboard, <@{membership.personId}>",
#     )

# --- Lab 4: send, edit, delete. See lab4/messages.py ---

# --- Lab 5: introductions and a message log. See lab5/bots.py ---

print("Uncomment the Lab 2 lines when you are ready to create the room.")
