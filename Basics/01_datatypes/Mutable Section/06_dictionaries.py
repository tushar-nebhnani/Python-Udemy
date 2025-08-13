"""
    Dictionary:
        order doesnt't matter in dictionaries.
        all the things in set are applied to dictionaries as well.
"""
chai_order = dict(type="Masala Chai", size="Large", sugar=2)
print(f"Chai order: {chai_order}")

chai_recipe = {}
chai_recipe["base"] = "black tea"
chai_recipe["liquid"] = "milk"

print(f"Chai Receipe: {chai_recipe}")
print(f"Chai Base: {chai_recipe['base']}")

del chai_recipe["liquid"]
print(f"Deleted Chai Receipe: {chai_recipe}")

chai_order = {
    "type": "ginger",
    "size": "small",
    "sugar": 2,
}

# print(f"Order details(keys): {chai_order.keys()}")
# print(f"Order details(values): {chai_order.values()}")
# print(f"Order details(items): {chai_order.items()}")

last_items = chai_order.popitem()
print(f"Last item: {last_items}")

extra_spices = {"cardamon": "crushed", "ginger":"sliced"}
chai_recipe.update(extra_spices)
print(f"Update chai receipe: {chai_recipe}")

# now the app won't crash completely, gets the thing to you in a safe manner without crashing the whole thing
cusotmer_note = chai_order.get("customer_note", "No note given")
print(f"chai size: {cusotmer_note}")

# membership testing
print(f"Is sugar in the order? {"suagr" in chai_order}")