flavours = ["Ginger", "Out of Stock", "Cardmon", "Lemon", "Discontinued", "Tulsi"]

for flavour in flavours:
    if flavour == "Out of Stock":
        continue
    if flavour == "Discontinued":
        break
    print(f"flavour is {flavour}.")

print("Out of Loop. Execution completed.")

