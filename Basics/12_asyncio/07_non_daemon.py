"""
    Sometimes the working of the thread is not completed but our main program completes.

    Daemon threads are the backgroung thread which shut down when the main program shuts down. Automatically shuts down when the main thread is gone.


    Profiling -> shows time for each function, where my main thread spent time in each one of them
    cmd -> python -m cProfile -s time 07_non_daemon.py
"""
import threading
import time

def monitor_tea_temp():
    while True:
        print("Monitoring tea teampreature...")
        time.sleep(2)

t = threading.Thread(target=monitor_tea_temp)
t.start()

print("Main program done.")