# Lab 1: REST APIs and JSON - solution (sample file, no network)

import json
from pathlib import Path

SAMPLE = Path(__file__).resolve().parent.parent / "rooms_sample.json"

with open(SAMPLE, encoding="utf-8") as file:
    data = json.load(file)

print("Keys in the response:", list(data.keys()))

rooms = data.get("items", [])
print("\nKeys and Values for Rooms:")
for i in range(5):
    room = rooms[i]
    print(f"Room ID: {room['id']}")
    print(f"Room Title: {room['title']}")
    print(f"Room Type: {room['type']}")
    print(f"Is Locked: {room['isLocked']}")
    print(f"Last Activity: {room['lastActivity']}")
    print(f"Creator ID: {room['creatorId']}")
    print(f"Created: {room['created']}")
    print(f"Is Public: {room['isPublic']}")
    print(f"Is Read Only: {room['isReadOnly']}")
    print()

with open("rooms.txt", "w", encoding="utf-8") as file:
    for room in rooms[:5]:
        file.write(room["title"] + "\n")
print("Wrote rooms.txt")
