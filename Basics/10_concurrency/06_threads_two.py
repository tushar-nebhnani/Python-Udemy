"""
    One CPU, One Core.
"""

import threading
import time

def prepare_Chai(type_, wait_time):
    print(f"{type_} Chai: brewing...")
    time.sleep(wait_time)
    print(f"{type_} Chai: brewed.")

start = time.time()

t1 = threading.Thread(target=prepare_Chai, args=("Masala", 2))
t2 = threading.Thread(target=prepare_Chai, args=("Ginger", 3))

t1.start()
t2.start()

t1.join()
t2.join()

end = time.time()

print(f"Total time: {end-start:.2f}")