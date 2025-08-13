# when you want to have continous update n constant log update then we use infinite generators
def infinite_chai():
    count = 1
    while True: # might drain the memory if we are not careful
        yield f"Refill #{count}"
        count += 1

refill = infinite_chai()

while True:
    print(next(refill))