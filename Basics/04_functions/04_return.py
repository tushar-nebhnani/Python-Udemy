def make_chai():
    return "Here! Is your masala tea."

return_value = make_chai()
print(return_value)
print(make_chai())

"""
    _ : when you want to handle unwanted value
"""

def ideal_func():
    pass

print(ideal_func()) # returns none value

def sold_cups():
    return 120

total = sold_cups()
print(total)

def chai_status(cups):
    if cups == 0:
        return "Sorry"
    return "Chai i sready"
    print(chai)

print(chai_status(0))