# Lab 7: The same echo bot, now with FastAPI

from contextlib import asynccontextmanager

import requests
from fastapi import FastAPI, Request

# TODO 1: Put your BOT token and bot email here (same bot as Lab 6).
bot_token = "YOUR_BOT_ACCESS_TOKEN"
bot_email = "YOUR_BOT_EMAIL"


def send_message(room_id, text):
    url = "https://webexapis.com/v1/messages"
    headers = {
        "Authorization": f"Bearer {bot_token}",
        "Content-Type": "application/json",
    }
    data = {"roomId": room_id, "text": text}
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        print("Message sent:", response.json().get("text"))
    else:
        print("Error sending message:", response.status_code, response.text)


# TODO 2: lifespan runs when the server starts, then waits, then shuts down.
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("FastAPI echo bot starting. Waiting for POST /webhook ...")
    yield
    print("FastAPI echo bot stopping.")


app = FastAPI(lifespan=lifespan)


@app.get("/")
async def home():
    return {"status": "Echo bot is running"}


# TODO 3: The webhook. FastAPI uses async def and await request.json().
@app.post("/webhook")
async def webhook(request: Request):
    data = await request.json()
    if data.get("resource") == "messages" and data.get("event") == "created":
        message_id = data["data"]["id"]
        if message_id == "test":
            print("Webhook reached (local test).")
            return {"status": "success"}
        headers = {"Authorization": f"Bearer {bot_token}"}
        message_url = f"https://webexapis.com/v1/messages/{message_id}"
        message_response = requests.get(message_url, headers=headers)
        if message_response.status_code == 200:
            message = message_response.json()
            if message.get("personEmail") != bot_email:
                send_message(message["roomId"], f"Echo: {message.get('text')}")
        else:
            print("Error retrieving message:", message_response.status_code)
    return {"status": "success"}


# Start it from the day2 folder:
#   uvicorn lab7.echo_fastapi:app --reload --port 8000
