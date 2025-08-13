"""
    Namespace: Each object has its own namespace like object, method, properties and it doesn't affect the original class.
"""

class Chai:
    is_hot = True  
    origin = "India" # referred as properties when they are inside the class


print(Chai)

masala = Chai()
print(f"Masala: {masala.origin}")
print(f"Masala: {masala.is_hot}")
masala.is_hot = False
print(f"Chai: {Chai.is_hot}")
print(f"Masala after waiting: {masala.is_hot}")
masala.Flavor = "Strong Adrak Chai"
print(masala.Flavor)