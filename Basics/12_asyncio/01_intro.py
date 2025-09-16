"""
    Async does only one thing which is, 'Declare a coroutine(special function that can be paused)'

    Async -> Await(Pause execution until the result is ready), await can only be applied when there is async.

    Gracefully wait for something to happen and until then we can serve some other thing gracefully, that's how it works without the use of threading, mulitprocessing.

    Asyncio -> built in python library.

    Event Loop. This is the engine that runs and schedules co-routine in python.
"""
import asyncio
import time

async def brew_chai():
    print("Brewing chai..")
    await asyncio.sleep(2) # it doesn't block the main thread
    print("Chai is ready.")

# asyncio.run(brew_chai())

async def brew(name):
    print(f"Brewing {name}...")
    await asyncio.sleep(2)
    # time.sleep(2)
    print(f"{name} chai is ready.")

# the sleep was of 2 second but combining all the operations.
async def main():
    # gather allows you to pass major coroutine function
    await asyncio.gather(
        brew("Masala Chai"),
        brew("Ginger Chai"),
        brew_chai(),
    )

asyncio.run(main())