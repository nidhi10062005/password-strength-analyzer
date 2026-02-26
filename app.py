import re

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


def main():
    while True:
        pwd = input("Enter a password (or 'quit' to exit): ").strip()
        if pwd.lower() in ("quit", "exit"):
            break

        score, feedback = evaluate_password(pwd)
        print(f"\nStrength: {score}/5")
        if feedback:
            print("Feedback:")
            for line in feedback:
                print(" -", line)
        print()

if __name__ == "__main__":
    main()