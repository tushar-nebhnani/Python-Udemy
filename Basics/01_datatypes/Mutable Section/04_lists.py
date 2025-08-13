"""
    List -> []
"""

ingredients = ["sugar", "water", "milk", "black tea masala"]
ingredients.append("salt")

print(f"Ingredients are: {ingredients}")
ingredients.remove("water")

spice_options = ["ginger", "cadamon", "salt"]
chai_ingredients = ["water", "milk"]

chai_ingredients.extend(spice_options)
print(f"chai ingredients: {chai_ingredients}")

chai_ingredients.insert(0, "tushar")
print(f"chai ingredients: {chai_ingredients}")

last_added = chai_ingredients.pop()
print(f"Last ingredient added: {last_added}")
chai_ingredients.reverse()
print(f"chai reverse: {chai_ingredients}")

chai_ingredients.sort()
print(f"sorted chai: {chai_ingredients}")

# Operator overloading

base_liquid = ["water", "milk"]
extra_flavours = ["ginger"]

full_liquid_mix = base_liquid + extra_flavours
print(f"Full liquid mix: {full_liquid_mix}")

strong_brew = ["black tea", "shot"] * 3
print(f"Strong Brew: {strong_brew}")

# list of just a string: treats every single ele as a list itself
raw_spice_data = bytearray(b"Cinnamon")
print(f"Raw Byte Data: {raw_spice_data}")
raw_spic_data = raw_spice_data.replace(b"cinna", b"card")
print(f"Raw Byte after replace Data: {raw_spic_data}")
