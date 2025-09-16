import asyncio
import aiohttp



async def fetch_url(session, url):
    async with session.get(url) as response:
        print(f"Fetched {url}: {response.status}")

async def main():
    URL = ["https://httpbin.org/delay/2"] * 3
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in URL]
        # tasks = [t1, t2, t3]
        await asyncio.gather(*tasks) # *tasks => unpacking things on the go

asyncio.run(main())

"""
    BLOCKING -> time.sleep(2) 
            VS 
    NON-BLOCKING -> await asyncio.sleep(2)
"""