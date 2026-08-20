import os
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/ai", methods=["POST"])
def ai_assistant():

    data = request.get_json() or {}

    message = data.get("message", "")
    feature = data.get("feature", "chatbot")

    if not message.strip():
        return jsonify({
            "error": "Please enter a message."
        }), 400

    # AI connection will be added securely later.
    response = (
        "AMANDA AI prototype\n\n"
        f"Feature: {feature}\n\n"
        f"Your request:\n{message}\n\n"
        "The real AI model connection will be activated "
        "after the private API key is configured."
    )

    return jsonify({
        "response": response
    })


@app.route("/api/health")
def health():

    return jsonify({
        "status": "AMANDA AI is running",
        "ai_connected": False
    })


if __name__ == "__main__":
    app.run()
