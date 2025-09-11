# __init__ -> creating a constructor via init
class ChaiOrder:
    def __init__(self, type_, size): # constructor
        self.type = type_
        self.size = size

    def summary(self):
        return f"{self.size}ml of {self.type} chai."      
    
order = ChaiOrder("Ginger", 100)
print(order.summary())

order_2 = ChaiOrder("Masala", 120)
print(order_2.summary())