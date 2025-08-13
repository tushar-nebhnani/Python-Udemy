staff = [("Amit", 16), ("Zara", 17), ("Raj", 15)]

# else statement is part of the for loop -> fallback logic
for name, age in staff:
    if age <= 18:
        print(f"{name} is eligible to manage the staff.")
        break
else:
    print(f"No one is eligible to manage.")