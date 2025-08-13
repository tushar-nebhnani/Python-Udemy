menu = ["Green Tea", "Lemon Tea", "Masala Tea", "Mint Tea"]

# .enumerate() -> provide numbers to the item in the list.
for item in menu:
    print(f"Menu item is: {item}.")

for item in enumerate(menu):
    print(f"{item}")

for idx, item in enumerate(menu, start = 1):
    print(f"{idx} : {item}")
