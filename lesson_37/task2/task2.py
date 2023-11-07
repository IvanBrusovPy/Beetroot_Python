import json
import aiohttp
import asyncio

json_data = 0


async def main():
    url = 'https://jsonplaceholder.typicode.com/posts'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as responce:
            global json_data
            json_data = await responce.json()
    with open("data.json", 'w') as f:
        json.dump(json_data, f)


asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())  # Фіксить проблему при запуску
asyncio.run(main())
