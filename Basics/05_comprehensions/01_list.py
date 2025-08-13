"""
Comprehensions are smart way to create list, set, dictionaries or generators in python using a single line of code.

We use them to filter item, transform item, create a new collection, flatten nested structure.

Purpose:
- Cleaner code
- faster execution

Types:
1. List
2. Set
3. Dictionary
4. Generator
"""

# List comprehensions: [expression for item in iterable if condition]
menu = [
    "Masala Chai",
    "Iced lemon Chai",
    "Green tea",
    "Iced peach",
    "Ginger alvo"
]

iced_tea = [tea for tea in menu if "Iced" in tea]
print(iced_tea)

