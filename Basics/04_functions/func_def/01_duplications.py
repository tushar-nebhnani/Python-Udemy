"""
    Functions: readability, traceability, maintainability
"""

# reducing code duplications
def tea_stall(name, chai_type): # parameters
    return f"Order {chai_type.lower().capitalize()}, for {name.lower().capitalize()}."

print(tea_stall("tushar", "Masala Chai")) # arguments
print(tea_stall("hITeSH", "GiNGeR Chai"))