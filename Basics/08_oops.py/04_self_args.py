class Chaicup:
    size = 150 #ml

    def describe(self):
        return f"THe size of the cup is {self.size}ml."

cup = Chaicup()
# cup.describe()
# print(Chaicup.describe()) # it cannot call itself
print(Chaicup.describe(cup))

cup_two = Chaicup()
cup_two.size = 100
# print(cup_two.describe())
print(Chaicup.describe(cup_two))