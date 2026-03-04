import re

def check_password_strength(password):
    score = 0

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        print("❌ Password should be at least 8 characters long")

    # Uppercase check
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        print("❌ Add at least one uppercase letter")

    # Lowercase check
    if re.search(r"[a-z]", password):
        score += 1
    else:
        print("❌ Add at least one lowercase letter")

    # Digit check
    if re.search(r"[0-9]", password):
        score += 1
    else:
        print("❌ Add at least one number")

    # Special character check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        print("❌ Add at least one special character")

    # Strength result
    if score == 5:
        print("✅ Strong Password")
    elif score >= 3:
        print("⚠️ Medium Strength Password")
    else:
        print("❌ Weak Password")


password = input("Enter your password: ")
check_password_strength(password)
