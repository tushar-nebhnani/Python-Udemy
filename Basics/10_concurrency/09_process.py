from multiprocessing import Process
import time

def cpu_heavy():
    print(f"Crunching some numbers....")
    t = 0
    for i in range(100_000):
        t+=i 
    print("Done")


if __name__ == '__main__':
    start = time.time()

    process = [Process(target=cpu_heavy) for _ in range(2)]
    [t.start() for t in process]
    [t.join() for t in process]

    end = time.time()

    print(f"Total time: {end-start:.2f}")
