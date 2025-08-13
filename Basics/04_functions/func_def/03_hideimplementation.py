def register_user():
    return f"{get_input()}\n{validate_input()}\n{save_to_db()}\nUser registration completed."

def get_input():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    address = input("Enter your address: ")
    return "Registration Completed."

def validate_input():
    return f"Validating the user info."

def save_to_db():
    return f"Data is being save to database."


print(register_user())