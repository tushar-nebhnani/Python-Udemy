"""
    Just Experience It!
    Coding is some process which you do and get over with, It's journery where you live, fail, suceed, die and all over again but its journey worth going on.

    Points to Remenber:
    1. The len() function in python only returns the length of the unique elements in python.
    2. Dictionaries are ordered in Python 3.7+. Dictionaries maintain insertion order in Python 3.7 and later versions, which is a key characteristic of their design.
    3. A key rule is that dictionary keys must be immutable. This means you cannot use mutable objects like a list as a key. The reason is that dictionaries use a process called hashing to quickly find a value based on its key, and a mutable object's hash value can change, which would break the dictionary's lookup system. You're right that a list of values can be used as a value in a dictionary, though!
    4. You are correct that the tuple itself is immutable. You cannot reassign an element of the tuple, for example, x[2] = [3, 5] would raise an error. However, the immutability of the tuple only applies to its direct contents. The list [3, 4] is a mutable object, and the tuple's immutability doesn't prevent you from changing the contents of that list.
    5. For x = (5), the variable x is an integer. The parentheses are simply used for grouping, just as they would be in a mathematical expression like (2 + 3). The interpreter evaluates (5) to 5. For x = (5,), the variable x is a tuple. The comma after the element is what tells Python to treat the expression as a tuple with a single element.





    Questions to visit again:
    1. What will be the output of `type(type(10))`?
    2. In a Python dictionary, what is the main rule regarding its keys? For example, can a list be a key in a dictionary? Why or why not?
    3. Can you explain the difference between the / operator and the // operator in Python?
    4. If you have a variable x = (1, 'two', [3, 4]), which contains a tuple with a list inside it, is it possible to change the value 4 to 5? Why or why not?
"""
x = (1, 'two', [3,4])
x[2][1] = 5
print(x)