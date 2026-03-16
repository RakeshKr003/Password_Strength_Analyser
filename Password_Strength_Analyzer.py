import re


# Analyze the strength of a password and return a short message.
def analyze_password_strength(password: str) -> str:
    """Return a string describing password strength.

    Rules (simple):
    - at least 8 characters
    - at least one uppercase letter
    - at least one lowercase letter
    - at least one digit
    - at least one special character from @#$%^&*! or similar
    """
    if not isinstance(password, str) or password == "":
        return "Invalid input: password must be a non-empty string."

    if len(password) < 8:
        return "Weak password: must be at least 8 characters long."
    if not re.search(r"[A-Z]", password):
        return "Weak password: include at least one uppercase letter."
    if not re.search(r"[a-z]", password):
        return "Weak password: include at least one lowercase letter."
    if not re.search(r"[0-9]", password):
        return "Weak password: include at least one digit."
    # check for presence of at least one special character
    if not re.search(r"[@#$%^&*!]", password):
        return "Weak password: include at least one special character (e.g. @ # $ % ^ & * !)."

    return "Strong password."


if __name__ == "__main__":
    try:
        user_password = input("Enter your password to check its strength: ")
    except (KeyboardInterrupt, EOFError):
        print("No input received.")
    else:
        print(analyze_password_strength(user_password))





