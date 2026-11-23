# Lab 6: A Flask echo bot - solution

from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

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
            if message.get("personEmail") != bot_email:
                send_message(message["roomId"], f"Echo: {message.get('text')}")
        else:
            print("Error retrieving message:", message_response.status_code)
    return jsonify({"status": "success"}), 200


@app.route("/", methods=["GET"])
def home():
    return "Echo bot is running. POST /webhook is waiting for Webex."


if __name__ == "__main__":
    app.run(port=5000)
