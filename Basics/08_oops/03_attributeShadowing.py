"""
    When variable is inside a class we call it as attribute. And function becomes method just like that.
"""

class Chai:
    tempreature = "Hot"
    strength = "Strong"

cutting = Chai()
print(cutting.tempreature) # Hot
cutting.tempreature = "Mild"
cutting.cup = "Small"

print(f"After changing: {cutting.tempreature}") # Mild
print(f"Direct look into the class: {Chai.tempreature}") # Hot

print("After Deleting")
del cutting.tempreature
del cutting.cup
"""
    If the refernce of object attribute doesn't exists anymore is will simply fallback to the original reference. If the fallback is present in the class it will goes back to normal, otherwise if that is not the case it will show "class has no attributes".
"""
print(f"After changing: {cutting.tempreature}")
#print(f"After changing: {cutting.cup}")
"""
    File "D:\Udemy\Python-Udemy\Basics8_oops\_attributeShadowing.py", line 24, in <module>
    print(f"After changing: {cutting.cup}")
                             ^^^^^^^^^^^
    AttributeError: 'Chai' object has no attribute 'cup'
"""
print(f"Direct look into the class: {Chai.tempreature}")