"""
    Strings are sequence of characteres which are enclosed in quotes.
    Immutable in nature. Indexing always starts from zero.
    In the world of python, the last numbers is not inclusive in slicing/indexing etc. etc.
    Slicing -> string[start: end: step-up]
"""

str1 = "hello"
print(f"Intial ID of string: {id(str1)}")
str2 = "hello" # reference of the value in assign to the variable in the memory
print(f"Intial ID of string: {id(str2)}")
str1 = "world"
print(f"ID of string: {id(str1)}")

chai_description = "Aromatic and Bold in taste"
print(f"First word of chai_description: {chai_description[:8]}")
print(f"Last word of chai_description: {chai_description[12:]}")
print(f"Reverse of the string: {chai_description[::-1]}")

lable_text = "Café, naïve, résumé, piñata, 你好, 😊"
encoded_label = lable_text.encode("utf-8")
decoded_label = encoded_label.decode("utf-8")
print(f"Non-encoded label: {lable_text}")
print(f"encoded label: {encoded_label}")
print(f"Decoded label: {decoded_label}")