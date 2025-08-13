# sometimes generator doesn't yield the value on its own, it needs something to yield from somewhere

# YIELD FROM 
def local_chai():
    yield "Masala Chai"
    yield "Ginger Chai"

def imported_chai():
    yield "Matcha Chai"
    yield "Oolong Chai"

def full_menu():
    yield from local_chai()
    yield from imported_chai()

for chai in full_menu():
    print(chai)

def chai_stall():
    try:
        while True:
            order = yield "Waiting for chai order!"
    except:
        print("Stall closed there is no more chai.")

stall = chai_stall()
print(next(stall))
stall.close() # we should always make sure to close our generators 