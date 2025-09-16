import asyncio
import time
from concurrent.futures import ThreadPoolExecutor #similar to asyncio.gather() but for threads

def check_stock(item):
    print(f"Checking {item} in store...")
    time.sleep(2) # Blocking Operation
    return f"{item} stock: 42"

# async is another tool in the belt it is not a replacement for anytings, it just makes thing better.

# This does not block our main thread, it is executing on a whole new thread.
async def main():
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool:
        result = await loop.run_in_executor(pool, check_stock, "Masala Chai")
        print(result)

asyncio.run(main())