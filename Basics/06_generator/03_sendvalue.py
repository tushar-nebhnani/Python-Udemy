# yields are kinda like traffic police officer
def chai_customer():
    print("Welcome! What chai would you like to have?")
    order = yield # yield flows like a stream, so we can store values because until one action is not performed it won't makes the execution move forward. SO, my order is expecting value through yield
    while True:
        print(f"Preparing: {order}")
        order = yield # for new order, we will take a new order contiously without altering the program. Acts like a incrementor, yields stops the flow of the loop.

stall = chai_customer() # iterable object
next(stall) # start the whole generation process
# yield pauses flow if program

stall.send("Masala Chai")
stall.send("Adrak Chai")
stall.send("Ginger Chai")