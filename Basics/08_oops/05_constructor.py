"""
    Initialisation -> __init__: When every object doesn't want to have default values. Objects want to have there own properties so we use __init__, this initialise the constructor which helps to set property in the function. 
"""
class ChaiOrder:
    # __init__ always comes with self.
    # we pass type_ because 'type' is a reserved keyword
    def __init__(self, type_, size): # constructor
        self.type = type_
        self.size = size

    def summary(self):
        return f"{self.size}ml of {self.type} chai."      
    
order = ChaiOrder("Ginger", 100)
print(order.summary())

order_2 = ChaiOrder("Masala", 120)
print(order_2.summary())