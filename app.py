import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/email", methods=["POST"])
def generate_email():
    data = request.get_json() or {}

    message = data.get("message", "")
    tone = data.get("tone", "Professional")

    if not message.strip():
        return jsonify({
            "error": "Please enter what you would like the email to say."
        }), 400

    email = f"""Subject: Regarding Your Request

Dear Recipient,

{message}

Kind regards,
Amanda
"""

    return jsonify({
        "email": email,
        "tone": tone
    })


@app.route("/api/health")
def health():
    return jsonify({
        "status": "AMANDA AI is running",
        "ai_connected": bool(os.getenv("AI_API_KEY"))
    })


if __name__ == "__main__":
    app.run(debug=True)
