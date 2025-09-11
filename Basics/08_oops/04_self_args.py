class Chaicup:
    size = 150 #ml

    # SELF: self is a reference to all the paramters we are definning within the class.
    def describe(self): # passing a paramter self
        return f"The size of the cup is {self.size}ml."

cup = Chaicup()
cup.describe()
# print(Chaicup.describe()) # it cannot call itself as it doesn't have the self argument
# TypeError: Chaicup.describe() missing 1 required positional argument: 'self'
print(Chaicup.describe(cup)) # Here, we are passing the context of the class

cup_two = Chaicup()
cup_two.size = 100
# Here, the describe function has got reference to it, the self attribute(parameter)
print(cup_two.describe()) 
print(Chaicup.describe(cup_two))