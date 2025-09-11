"""
Decorators: Decorators are nothing but too decorate something, they can be functional too. Add wrappers to a function.
Just a wrapper function which takes the function and add something more to it.
"""
from functools import wraps

def my_decorator(func):
    @wraps(func) # preserves the name of the function
    def wrapper():
        print("Before function runs.")
        func()
        print("After function runs.")
    return wrapper

@my_decorator
def greet():
    print("Hello World!")

greet()
print(greet.__name__)