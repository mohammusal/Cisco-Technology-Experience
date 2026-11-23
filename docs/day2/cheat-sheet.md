---
hide:
  - navigation
  - toc
---

# Day 2 cheat sheet

<p class="no-print" markdown>APIs, Webex and the two web servers. Print with ++ctrl+p++ (Mac ++cmd+p++).</p>

<div class="cheat" markdown>

<div markdown>
Install (once, in `.venv`)

```bash
python -m pip install requests webexteamssdk flask fastapi uvicorn
```
</div>

<div markdown>
Token file

```text
code/day2/token.txt     # you
code/day2/bot_token.txt # the bot
```

Never paste tokens into `.py` files.
</div>

<div markdown>
Load the token

```python
from config import access_token
token = access_token()
```
</div>

<div markdown>
GET rooms

```python
import requests
url = "https://webexapis.com/v1/rooms"
headers = {"Authorization": f"Bearer {token}"}
r = requests.get(url, headers=headers)
print(r.status_code)
rooms = r.json().get("items", [])
```
</div>

<div markdown>
HTTP verbs

```text
GET     read data
POST    create new
PUT     update existing
DELETE  remove
```
</div>

<div markdown>
Status codes

```text
200  OK
401  bad or expired token
404  id not found
409  already exists
```
</div>

<div markdown>
JSON

```python
data["items"][0]["title"]
```
</div>

<div markdown>
SDK: room and message

```python
from webexteamssdk import WebexTeamsAPI
api = WebexTeamsAPI(access_token=token)
room = api.rooms.create(title="Group 1")
api.messages.create(roomId=room.id, text="Welcome!")
```
</div>

<div markdown>
Add a member

```python
api.memberships.create(
    roomId=room.id,
    personEmail="ola@example.com",
    isModerator=True,
)
```
</div>

<div markdown>
Mention

```python
api.messages.create(
    roomId=room.id,
    markdown=f"Welcome onboard, <@{person_id}>",
)
```
</div>

<div markdown>
Edit (PUT) and delete

```python
requests.put(
    f"https://webexapis.com/v1/messages/{id}",
    headers=headers,
    json={"roomId": room_id, "text": "edited"},
)
api.messages.delete(id)
```
</div>

<div markdown>
Flask

```python
@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    return {"status": "success"}
```

```bash
python lab6/echo_flask.py
```
</div>

<div markdown>
FastAPI

```python
@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()
    return {"status": "success"}
```

```bash
python -m uvicorn lab7.echo_fastapi:app --reload --port 8000
```
</div>

<div markdown>
Do not echo yourself

```python
if message["personEmail"] != bot_email:
    send_message(...)
```
</div>

</div>
