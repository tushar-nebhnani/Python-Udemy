class BaseChai:
    def __init__(self, type_):
        self.type_ = type_

    def prepare(self):
        print(f"Preparing: {self.type_} chai ...")

class MasalaChai(BaseChai):
    def add_species(self):
        print(f"Adding cardamon, ginger & cloves.")

class ChaiShop():
    # Composition
    chai_cls = BaseChai # reference of the base chai

    def __init__(self):
        self.chai = self.chai_cls("Regular") # here the reference is passed to the chai. Internally (chai -> chai_cls -> BaseClass -> prepare)

    def serve(self):
        print(f"Serving: {self.chai.type_} chai ...")
        self.chai.prepare()

class FancyChaiShop(ChaiShop):
    chai_cls = MasalaChai

# Object are always created with the help of the constructor.
shop = ChaiShop()
fancy = FancyChaiShop()
shop.serve()
fancy.serve()
fancy.chai.add_species()
