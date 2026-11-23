# Lab 5: Bots, introductions, and a message log

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from config import access_token

from webexteamssdk import WebexTeamsAPI

api = WebexTeamsAPI(access_token=access_token())

# TODO 1: Paste the Room ID from room_details.txt.
room_id = "PASTE_ROOM_ID_HERE"

# TODO 2: After you create a bot at https://developer.webex.com/docs/bots,
# put the bot's email here (it looks like mybot@webex.bot).
bot_email = "mybot@webex.bot"

# TODO 3: Add the bot to the common room as a participant (not a moderator).
# api.memberships.create(roomId=room_id, personEmail=bot_email, isModerator=False)
# print("Bot added:", bot_email)

# TODO 4: Send YOUR introduction. Change the text, then run.
# api.messages.create(
#     roomId=room_id,
#     text="Hi, I am Ola from Krakow and I like Python.",
# )
# print("Introduction sent. Wait until everyone in the group has done this.")

# TODO 5: List the messages and write them to a file.
# lines = []
# for message in api.messages.list(roomId=room_id):
#     who = message.personEmail or "unknown"
#     text = message.text or ""
#     lines.append(f"{who}: {text}")
# Path("messages.txt").write_text("\n".join(lines), encoding="utf-8")
# print(f"Wrote {len(lines)} messages to messages.txt")
