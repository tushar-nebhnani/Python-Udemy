"""
    Sometimes the working of the thread is not completed but our main program completes.

    Daemon threads are the backgroung thread which shut down when the main program shuts down. Automatically shuts down when the main thread is gone.
"""
import threading
import time

def monitor_tea_temp():
    while True:
        print("Monitoring tea teampreature...")
        time.sleep(2)

t = threading.Thread(target=monitor_tea_temp, daemon=True)
t.start()

print("Main program done.")