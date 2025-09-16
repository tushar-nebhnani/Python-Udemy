# This is a race condition and you will never know that which thread will execute, that's why it is a highly unreliable peice of code

import threading
chai_stock = 0

def restock():
    global chai_stock 
    for _ in range(100_000):
        chai_stock += 1

threads = [threading.Thread(target=restock) for _ in range(2)]

for t in threads: t.start()
for t in threads: t.join()

print(f"Chai Stock: {chai_stock}")