"""
GENERATORS: a generator is a function or expression that creates an iterator, which is an object that you can loop over. The key characteristic of generators is that they produce values lazily, one at a time, rather than creating an entire sequence and storing it in memory.LIKE A STREAM: GENERATE ONE BY ONE. save memory. you don't want the results immediately. lazy evaluation.

yield keyword: This is the core of a generator function. Unlike return, which exits a function and returns a single value, yield pauses the function's execution, returns a value, and saves its state. When the generator is called again, it resumes execution from where it left off.Top the execution and resume only when the function is called, remenber tha place where it stopped

Key Points of generators: 
-> you save memory
-> and you don't want the result immediately
-> lazy evaluation
"""

def serve_chai():
    yield "Cup 1: Masala Chai"
    yield "Cup 2: Ginger Chai"
    yield "Cup 3: Elaichi Chai"

# here yield will return one by one

stall = serve_chai() # iterable object which is created by the generator
print(stall) # store reference to the memory, where our yield is stored

for cup in stall: # here, we are iterating on the object to get all the yield we created because if we called the yield once, it will stop then wait for the another call once we call it again, it will keep up again from where it stopped. 
    print(cup)

def get_chai_list():
    return ["Cup 1", "Cup 2", "Cup 3"]

def get_chai_gen():
    yield "Cup 1"
    yield "Cup 2"
    yield "Cup 3"

print(get_chai_list())
# print(get_chai_gen()) # the reference of the generatr object we got.

chai = get_chai_gen() # iterable object
# print(chai)
print(next(chai))
# print(next(chai))
print(next(chai))
# print(next(chai)) give error: because there is no other object in the sequence, the moment the yield stop last time was the moment when there was nothing left to execute.