from multiprocessing import Process
import time

def crunch_num():
    print(f"Started count process.. ")
    c = 0
    for i in range(100_000_000):
        c+=1
    print(f"Ended count process")

if __name__ == "__main__":
    
    start = time.time()

    p1 = Process(target=crunch_num)
    p2 = Process(target=crunch_num)

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    end = time.time()

    print(f"Total Time: {end - start:.2f} secs.")
