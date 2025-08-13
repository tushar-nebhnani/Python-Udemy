# Everything in python is a type of object.
class Chai:
    pass

class ChaiTime:
    pass

print(type(Chai))

ginger_tea = Chai() # Object of chai class
print(type(ginger_tea))
print(type(ginger_tea) is Chai)
print(type(ginger_tea) is ChaiTime)
