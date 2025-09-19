"""
    Offline Note Taker
"""

import json
import os 
from cryptography.fernet import Fernet
from datetime import datetime

VAULT_FILE = "notes_vault.json"
KEY_FILE = "vault.key"

def load_or_create_key():
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()

        with open(KEY_FILE, "wb") as f:
            f.write(key)
    
    else:
        with open(KEY_FILE, "rb") as f:
            key = f.read()
    return Fernet(key)

fernet = load_or_create_key()

def load_vault():
    if not os.path.exists(VAULT_FILE):
        return []

    with open(VAULT_FILE, "r", encoding="utf-8") as f:
        return json.load()
    
def save_vault(data):
    with open(VAULT_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def add_note():
    title = input("Enter note title: ").strip()
    content = input("Enter note content: ").strip()

    encrypted_content = fernet.encrypt(content.encode()).decode()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    data = load_vault()
    data.append({
        "title": title,
        "content": encrypted_content,
        "timestamp": timestamp,
    })

    save_vault(data)
    print("✅ Data Saved.")

def list_notes():
    data = load_vault()
    if not data:
        print("No notes present.")
        return
    for i, note in enumerate(data, 1):
        print(f"{i}. {note['title']} {note['timestamp']}")

def view_note(note):
    list_notes()
    try:
        idx = int(input("Enter note number to view: ")) - 1
        data = load_vault()
        if 0 <= idx <= len(data):
            encrypted = data[idx]["content"]
            decrypted = fernet.decrypt(encrypted.encode()).decode()
            print(f"\n {data[idx]['title']} - {data[idx]['timestamp']} - {decrypted}") 
        else:
            print("Invalid Selection.")
    except:
        print("ERROR OCCURED.")

def search_note():
    keyword = input("Enter the keyword: ").strip().lower()
    data = load_vault()
    found = [note for note in data if keyword in note["title"].lowwer()]
    if not found:
        print("No match found.")
    else:
        for note in found:
            print(f"{note['title']} = {note['content']}")

def main():
    while True:
        print("OFFLINE NOTES LOCKER\n1. Add Note\n2. View Note\n3. List Note\n4. Search Note\n5. Exit")

        choice = input("Enter your choice: ").strip()

        match choice:
            case '1':
                add_note()
            case '2':
                view_note()
            case '3':
                list_notes()
            case '4':
                search_note()
            case '5':
                exit()

if __name__ == "__main__":
    main()