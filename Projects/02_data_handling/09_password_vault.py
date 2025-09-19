"""
    CLI to manage login credentials for website.
    View & Update not working.
"""

import base64
import os 

VAULT_FILE = "vault.txt"

def encode(text):
    # .decode() is used to convert into string
    return base64.b64encode(text.encode()).decode()

def decode(text):
    return base64.b64encode(text.encode()).decode()

def password_strength(password):
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_unique = any(c in "!@#$%^&*().,<>" for c in password)

    score = sum([length >= 8, has_upper, has_digit, has_unique])
    return ["Weak", "Medium", "Strong", "Execellent"][min(score, 3)]

def add_credentials():
    website = input("Website: ").strip()
    username = input("Username: ").strip()
    password = input("Password: ").strip()
    
    strength = password_strength(password)

    line=f"{website}||{username}||{password}"
    encoded_line = encode(line)

    with open(VAULT_FILE, 'a', encoding="utf-8") as f:
        f.write(encoded_line + "\n")
    print("✅ Credentials Saved.")

def view_credentials():
    if not os.path.exists(VAULT_FILE):
        print("File not found")
        return
    
    with open(VAULT_FILE, 'r', encoding="utf-8") as f:
        for line in f:
            decoded = decode(line.strip())
            website, username, password = decoded.split('||')
            hidden_password = '*' * len(password)
            line=f"{website} | {username} | {password}"

def update_password(password):
    pass

def main():
    while True:
        print("Credential Manger\n1. Add Password\n2. View Password\n3. Update\n4. Exit")

        choice = input("Enter your choice: ")
        match choice:
            case '1':
                add_credentials()
            case '2':
                view_credentials()
            case '3':
                update_password()
            case '4':
                exit()

if __name__ == "__main__":
    main()