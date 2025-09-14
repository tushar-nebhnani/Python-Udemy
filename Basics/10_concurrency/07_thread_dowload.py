import requests
import threading
import time

def dowload(url):
    print(f"Starting dowload from {url}.")
    response = requests.get(url)
    print(f"Finished dowload from {url} of size: {len(response.content)} bytes.")

urls = [
    "https://httpbin.org/image/jpeg",
    "https://httpbin.org/image/png",
    "https://httpbin.org/image/svg",
]

start = time.time()
threads = []

for url in urls:
    t = threading.Thread(target=dowload, args=(url,))

    t.start()
    threads.append(t)

for t in threads:
    t.join()

end = time.time()

print(f"Total time taken to dowload: {end-start:.2f}")