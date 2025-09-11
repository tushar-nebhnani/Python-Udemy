# inheritance
class BaseChai:
    def __init__(self, type_):
        self.type = type_

    def prepare(self):
        print(f"Preparing {self.type} Chai....")

class MasalaChai(BaseChai):
    def add_spices(self):
        print("Adding cardamon, ginger, cloves.")      

class ChaiShope:
    chai_class = BaseChai # inheriting values of the base chai: Composition Syntax

    def __init__(self):
        self.chai = self.chai_class("Regular") 

    def serve(self):
        print(f"Serving {self.chai.type} in the shop.")
        self.chai.prepare()

class FancyChaiShop(ChaiShope):
    chai_cls = MasalaChai

shop = ChaiShope()
fancy = FancyChaiShop()
shop.serve()
fancy.serve()
fancy.chai.add_spices()