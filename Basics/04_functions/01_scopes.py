# Scope and Name Resolution
"""
    1. Local: Inside a function
    2. Enclosing from outer function if nested
    3. Global: Top level script
    4. Built in
"""
# Scope: The area in which we can access our variables.

# 1. local scope
def serve_chai():
    chai_type = "masala chai" # local scope
    print(f"Inside function: {chai_type}")


chai_type = "lemon chai" 
serve_chai()
print(f"Outside function: {chai_type}")

# 2. nested function
def chai_counter():
    chai_order = "lemon" # enclosing scope
    def print_order(): # declaring a function
        chai_order = "ginger"
        print("Inner: ", chai_order)
    print_order() # calling of the function
    print("Outer: ", chai_order)

chai_counter()

chai_order = "Tulsi" # Global
print(f"Global: ", chai_order)