"""
    When variable is inside a class we call it as attribute.
"""

class Chai:
    tempreature = "Hot"
    strength = "Strong"

cutting = Chai()
print(cutting.tempreature)
cutting.tempreature = "Mild"
cutting.cup = "Small"

print(f"After changing: {cutting.tempreature}")
print(f"Direct look into the class: {Chai.tempreature}")

print("After Deleting")
del cutting.tempreature
del cutting.cup
"""
    if the refernce of object attribute doesn't exists anymore is will simply fallback to the original reference. if the fallback exits in the class it will, otherwise it will show "class has no attributes".
"""
print(f"After changing: {cutting.tempreature}")
print(f"After changing: {cutting.cup}")
print(f"Direct look into the class: {Chai.tempreature}")