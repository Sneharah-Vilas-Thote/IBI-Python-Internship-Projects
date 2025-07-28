# Password-Generator-App.py

"""
Password Generator App
-----------------------
This simple Python app generates a strong random password using letters, digits, and symbols.
"""

import random
import string

def generate_password(length=12):
    if length < 6:
        return "❌ Password length too short. Use at least 6 characters."

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# -------- Main Program Starts Here --------

print("=== 🔐 Password Generator App ===")
try:
    user_length = int(input("Enter desired password length (minimum 6): "))
    result = generate_password(user_length)
    print(f"\n🧾 Your Generated Password: {result}\n")
except ValueError:
    print("\n❌ Invalid input! Please enter a valid number.\n")
