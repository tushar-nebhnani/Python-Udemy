essential_spices = {"cardamon", "ginger", "cinnamon"}
optional_spices = {"cloves", "ginger", "black pepper"}

all_spices = essential_spices | optional_spices # union
print(f"All spices: {all_spices}")

common_spices = essential_spices & optional_spices # intersection
print(f"Common Spices: {common_spices}")

only_in_essential = essential_spices - optional_spices
print(f"Only in esssential: {only_in_essential}")

# membership test
print(f"Is clove in essentil spices? {"cloves" not in essential_spices}")

# frozen set: immutable unordered set, working wise exactly the same