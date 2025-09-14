"""
    Command Line Based Contact Book 
    Will add an update method to in a while, more update are coming soon.
    Bug 1: When we add values in the csv, the values are added alternately. DEBUG.
"""
import csv
import os

FILENAME = "contacts.csv"

if not os.path.exists(FILENAME):
    with open(FILENAME, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow({"Name", "Phone", "Email"}) 

def add_contact():
    name  = input("Name: ").strip()
    phone = input("Phone: ").strip()
    email = input("Email: ").strip()

    # check for duplicate entries
    with open(FILENAME, 'r', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        for row in rows:
            if row["Name"].lower() == name.lower():
                print("Contact name already exists.")
                return
            
    with open(FILENAME, 'a', encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([name, phone, email])
        print("Contact Added.")

def view_contact():
    with open(FILENAME, 'r', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            print()
            print(f"Name: {row["Name"]} \nPhone: {row["Phone"]} \nMail: {row['Email']}")
            print()

def search_contact():
    term = input("Enter the name to search: ").strip().lower()
    found = False

    with open(FILENAME, 'r', encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if term in row["Name"].lower() == term:
                print(f"FOUND:\n{row['Name']} | {row['Phone']} | {row['Email']}")
                found = True

    if not found:
        print("No matching contact found.")

def main():
    while True:
        print("Contact Book")
        print("1. Add")
        print("2. View")
        print("3. Search")
        print("4. Exit")

        choice = int(input("Choose an option: "))
        if choice == 1:
            add_contact()
        elif choice == 2:
            view_contact()
        elif choice == 3:
            search_contact()
        elif choice == 4:
            break
        else:
            print("Invalid choice found.")

if __name__ == "__main__":
    main()