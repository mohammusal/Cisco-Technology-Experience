# Lab 1: REST APIs and JSON
# Run this file after each TODO. It works even before you change anything.

import json
from pathlib import Path

SAMPLE = Path(__file__).resolve().parent.parent / "rooms_sample.json"

# TODO 1: Load the sample JSON (this is what Webex would send you).
with open(SAMPLE, encoding="utf-8") as file:
    data = json.load(file)

print("Keys in the response:", list(data.keys()))

# TODO 2: Get the list of rooms and print the first 5.
# rooms = data.get("items", [])
# print("\nKeys and Values for Rooms:")
# for i in range(5):
#     room = rooms[i]
#     print(f"Room ID: {room['id']}")
#     print(f"Room Title: {room['title']}")
#     print(f"Room Type: {room['type']}")
#     print(f"Is Locked: {room['isLocked']}")
#     print(f"Last Activity: {room['lastActivity']}")
#     print(f"Creator ID: {room['creatorId']}")
#     print(f"Created: {room['created']}")
#     print(f"Is Public: {room['isPublic']}")
#     print(f"Is Read Only: {room['isReadOnly']}")
#     print()

# TODO 3: Write the titles to a file. Remove the # from the block below.
# with open("rooms.txt", "w", encoding="utf-8") as file:
#     for room in rooms[:5]:
#         file.write(room["title"] + "\n")
# print("Wrote rooms.txt")

# TODO 4: The real request. Remove the # only after Lab 0's token.txt is ready.
# import sys
# import requests
# sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
# from config import access_token
# url = "https://webexapis.com/v1/rooms"
# headers = {
#     "Authorization": f"Bearer {access_token()}",
#     "Content-Type": "application/json",
# }
# response = requests.get(url, headers=headers)
# print("Status of the Request:", response.status_code)
# if response.status_code == 200:
#     live = response.json()
#     for room in live.get("items", [])[:5]:
#         print(f"Live room: {room['title']}")
# else:
#     print("Failed to fetch room details. Status code:", response.status_code)
