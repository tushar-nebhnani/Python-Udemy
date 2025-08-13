# Walrus operator -> ":="
# x = 5 Statement: here we are just stating
# 3 + 3 = 6 Expression

# value = 13
# remainder = value % 5

# if remainder:
#     print(f"Not divisible, remainder is {remainder}")


value = 13

if (remainder := value % 5):
    print(f"Not divisible, remainder is {remainder}")


sizes = ["Small", "Medium", "Large"]
 
if (requested_size := input("Enter your cup size: ")) in sizes:
    print(f"Serving {requested_size}")
else:
    print(f"Size is not available - {requested_size}")


flavours = ["Garlic", "Masla", "Ginger", "Lemon", "Mint"]

print("Available flavours", flavours)

while (flavour := input("Choose your flavour: ")) not in flavours:
    print(f"Sorry, {flavour} is not available.")

print(f"You choose {flavour} chai")