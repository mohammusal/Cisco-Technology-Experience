# Lab 4: Send, edit and delete a message

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

# TODO 1: Paste the Room ID from room_details.txt.
room_id = "PASTE_ROOM_ID_HERE"

# TODO 2: Send a new message.
# message = api.messages.create(
#     roomId=room_id,
#     text="This is a draft. We will edit it in a moment.",
# )
# print("Created message id:", message.id)

# TODO 3: Edit that message (the SDK has no edit helper, so we use the REST API).
# edit = requests.put(
#     f"https://webexapis.com/v1/messages/{message.id}",
#     headers=headers,
#     json={
#         "roomId": room_id,
#         "text": "This message was edited by Python!",
#     },
# )
# print("Edit status:", edit.status_code)

# TODO 4: Delete it.
# api.messages.delete(message.id)
# print("Deleted the message.")
