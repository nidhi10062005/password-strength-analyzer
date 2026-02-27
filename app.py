from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)

COMMON_PASSWORDS = [
    "password", "123456", "123456789",
    "qwerty", "abc123", "password123",
    "admin", "letmein"
]

def evaluate_password(password):
    score = 0
    feedback = []

    if not password:
        feedback.append("Password cannot be empty.")
        return score, feedback

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("At least 8 characters required.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("Include at least one digit.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Include at least one special character.")

    if password.lower() in COMMON_PASSWORDS:
        feedback.append("This is a commonly used weak password.")
        score = 0

    return score, feedback

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/check_password", methods=["POST"])
def check_password():
    data = request.get_json()
    password = data.get("password", "")
    score, feedback = evaluate_password(password)
    return jsonify(score=score, feedback=feedback)

if __name__ == "__main__":
    # bind explicitly to localhost
    app.run(host="127.0.0.1", port=5000, debug=True)