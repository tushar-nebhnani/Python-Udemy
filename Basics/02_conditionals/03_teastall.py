name = input("Enter your name: ")
size = input("Enter your size (large/medium/small): ").lower()

if size == "large":
    print(f"{name}, Your bill is 20.")
elif size == "medium":
    print(f"{name}, Your bill is 10.")
elif size == "small":
    print(f"{name}, Your bill is 5.")
else:
    print("ERROR: Invalid cup size entered.")
    
    