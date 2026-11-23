# Lab 1 exercise: count room types from the sample JSON

import json
from pathlib import Path

SAMPLE = Path(__file__).resolve().parent.parent / "rooms_sample.json"

with open(SAMPLE, encoding="utf-8") as file:
    rooms = json.load(file).get("items", [])

group = 0
direct = 0
locked = 0
for room in rooms:
    if room["type"] == "group":
        group = group + 1
    elif room["type"] == "direct":
        direct = direct + 1
    if room["isLocked"]:
        locked = locked + 1

print(f"Rooms in the file: {len(rooms)}")
print(f"Group rooms: {group}")
print(f"Direct rooms: {direct}")
print(f"Locked rooms: {locked}")
