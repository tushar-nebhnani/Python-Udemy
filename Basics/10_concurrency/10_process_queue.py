from multiprocessing import Process, Queue, Value

queue = Queue()

def prepare_chai(queue):
    queue.put("Masala Chai is ready.")

counter = Value('i', 0) # automatically comes with an lock

if __name__ == '__main__':
    p = Process(target=prepare_chai, args=(queue,))
    p.start()
    p.join()
    print(queue.get())