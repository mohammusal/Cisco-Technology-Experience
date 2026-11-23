# Lab 6: A Flask echo bot
# This file starts a small web server. Stop it with Ctrl+C.

from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# TODO 1: Put your BOT token and bot email here (from the bot you created in Lab 5).
# This is the bot token, not your personal token.
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


# TODO 2: This is the doorbell. Webex knocks here when a message is created.
@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    if data.get("resource") == "messages" and data.get("event") == "created":
        message_id = data["data"]["id"]
        if message_id == "test":
            print("Webhook reached (local test).")
            return jsonify({"status": "success"}), 200
        headers = {"Authorization": f"Bearer {bot_token}"}
        message_url = f"https://webexapis.com/v1/messages/{message_id}"
        message_response = requests.get(message_url, headers=headers)
        if message_response.status_code == 200:
            message = message_response.json()
            # Do not reply to the bot's own messages (that would loop forever).
            if message.get("personEmail") != bot_email:
                send_message(message["roomId"], f"Echo: {message.get('text')}")
        else:
            print("Error retrieving message:", message_response.status_code)
    return jsonify({"status": "success"}), 200


# TODO 3: A tiny page so you can check the server in a browser.
@app.route("/", methods=["GET"])
def home():
    return "Echo bot is running. POST /webhook is waiting for Webex."


if __name__ == "__main__":
    # TODO 4: Run the server. Then send a POST to http://127.0.0.1:5000/webhook
    # with a sample JSON file (see the lab guide) before you try a real webhook.
    app.run(port=5000)
