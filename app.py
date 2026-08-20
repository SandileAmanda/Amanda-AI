from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/email", methods=["POST"])
def generate_email():
    data = request.get_json()

    message = data.get("message", "")
    tone = data.get("tone", "Professional")

    if not message.strip():
        return jsonify({
            "error": "Please enter what you would like the email to say."
        }), 400

    # Temporary response.
    # We will connect AMANDA AI to an AI model later.
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


if __name__ == "__main__":
    app.run(debug=True)
