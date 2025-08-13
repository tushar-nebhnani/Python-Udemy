name = input("Enter your name: ")
snack = input("Enter your choice: ").lower()

print(f"User choosed: {snack}")
if snack == "samosa" or snack == "cookies":
    print(f"Great Choice {name}! {snack} Order Confirmed.")
else:
    print(f"Sorry {name}! {snack} are not available right now.")