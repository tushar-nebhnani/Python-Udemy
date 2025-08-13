order = ["masala", 'ginger']
# print(order[2]) # IndexError
#  NameError, ZeroDivisionError, TypeError

chai_menu = {"masala": 30, "ginger": 50}
try:
    chai_menu["elaichi"] # KeyError 
except KeyError:
    print("⚠️  The key which you are trying to access does not exists.")