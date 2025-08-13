"""
    def function_name('arguments'):
        pass
        
    - args: argument, *kwargs: keyword argument
"""

chai = "Ginger Tea"
def prepare_chai(order):
    print(f"Preparing chai {order}")

prepare_chai(chai)

chai = [1,2,3]
def edit_chai(cuo):
    cuo[1] = 42

edit_chai(chai)
print(chai)

def make_chai(tea, milk, sugar):
    print(tea, milk, sugar)

make_chai("darjeeling", "yes", "no") # positional arguments
make_chai(tea="green", milk="no", sugar="2 cups") # keyword arguments

# *args, **kwargs
def special_chai(*ingredietnts, **extras):
    print("ingredient", ingredietnts)
    print("extra", extras)

special_chai("cinnamon", "ginger", sweetner = "sugar", milk = "low fat")

# def chai_order(order = []):
#     order.append("Small")
#     print(order)

def chai_order(order = None):
    if order is None:
        order = []
    print(order)

# default traps
chai_order()
chai_order()