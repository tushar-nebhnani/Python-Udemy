import threading
c = 0
lock = threading.Lock()

def increment():
    global c
    for _ in range(100_000_000):
        with lock:
            c += 1

threads = [threading.Thread(target=increment) for _ in range(10)]
[t.start() for t in threads] 
[t.join() for t in threads] 

print(f"Final Counter: {c}")