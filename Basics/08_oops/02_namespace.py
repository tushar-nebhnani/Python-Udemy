"""
    Namespace: Each object has its own namespace like method, functions,properties and it doesn't affect the original class methods, properties of the Class Created.
"""

class Chai:
    is_hot = True  
    origin = "India" # referred as properties when they are inside the class


print(Chai)

masala = Chai()
print(f"Masala: {masala.origin}") # India
print(f"Masala: {masala.is_hot}") # True
masala.is_hot = False
print(f"Chai: {Chai.is_hot}") # True
print(f"Masala after waiting: {masala.is_hot}") # False
masala.Flavor = "Strong Adrak Chai"
print(masala.Flavor)