import re

def check_password_strength(password):
    length = len(password) >= 8
    upper = re.search(r"[A-Z]", password)
    lower = re.search(r"[a-z]", password)
    digit = re.search(r"[0-9]", password)
    special = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)

    if length and upper and lower and digit and special:
        return "Strong Password ✅"
    elif length and (upper or lower) and digit:
        return "Medium Password ⚠️"
    else:
        return "Weak Password ❌"

password = input("Enter your password: ")
result = check_password_strength(password)
print(result)