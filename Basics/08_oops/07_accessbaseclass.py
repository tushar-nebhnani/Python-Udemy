class Chai:
    def __init__(self, type_, strength):
        self.type = type_
        self.strength = strength

class GingerChai(Chai):
    # def __init__(self, type_, strength, spice_level):
            # Code duplication
    #     self.type = type_
    #     self.strength = strength
    #     self.spice_level = spice_level

    # def __init__(self, type_, strength, spice_level):
        # Explicit Call 
    #     Chai.__init__(self, type_, strength)
    #     self.spice_level = spice_level

    def __init__(self, type_, strength, spice_level):
        super().__init__(type_, strength) # This automatically means that i am going to call the constructor of the base class
        self.spice_level = spice_level
        