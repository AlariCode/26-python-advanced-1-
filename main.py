import asyncio
import aiohttp

# Получение в задачам параллельно 10 раз обращение к google


async def main():
    urls = ["https://google.com"] * 20
    async with aiohttp.ClientSession() as session:
        tasks = [
            session.get(url) for url in urls
        ]
        results = await asyncio.gather(*tasks)
        print(list(map(lambda x: x.status, results)))

asyncio.run(main())
