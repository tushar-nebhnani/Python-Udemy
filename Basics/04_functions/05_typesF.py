"""
Types of functions:
    1. Lambda functions <anonymous>
    2. pure vs impure functions
    3. recurrsive functions
"""

def pure_chai(cups): # doesn't alter any ingredient globally
    return cups * 10

total_chai = 0

# Not Recomended
def impure_chai(cups): # alter the global variable
    global total_chai
    total_chai * 10


def pour_chai(n):
    if n == 0 :
        return "All cups poured"
    return pour_chai(n-1)

pure_chai(30)

chai_types = ["Light", "Strong", "Ginger", "Strong"]

strong_chai = list(filter(lambda chai: chai != "Strong", chai_types))
print(strong_chai)