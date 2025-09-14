"""
    Global Interpreter Lock(GIL)

    Race Condition: When two thread wants to change the same memory location and which thread will change the memory?

    MUTEX: the moment a thread reach memory it will get mutex which is GIL, so that any other thread cannot access the memory until the execution is completed.
"""
import threading
import time

def brew_chai():
    print(f"{threading.current_thread().name} started brewing...")
    c = 0
    for _ in range(100_000_000):
        c+=1
    print(f"{threading.current_thread().name} finished brewing.")

thread1 = threading.Thread(target=brew_chai, name="Barits-1")
thread2 = threading.Thread(target=brew_chai, name="Barits-2")

start = time.time()
thread1.start()
thread2.start()
thread1.join()
thread2.join()
end = time.time()

print(f"Total time: {end - start:.2f} secs")
