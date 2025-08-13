# Set comprehensions: {expression for item in iterable if condition}

flavours = [
    "Masala Chai", "Green Tea", "Masala Chai",
    "Ginger", "Green Tea", "Adrak"
]

unique_flavours = {tea for tea in flavours}
print(unique_flavours)


recipes = {
    "Masala Chai": ["ginger", "adrak", "cardamon", "clove"],
    "Elachi Chai": ["cardamon", "milk"],
    "Spicy Chai": ["ginger", "black pepper", "clove"],
}

unique_spices = {spice for ingredients in recipes.values() for spice in ingredients}
print(unique_spices)