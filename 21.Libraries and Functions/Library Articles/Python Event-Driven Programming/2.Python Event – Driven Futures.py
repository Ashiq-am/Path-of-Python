import asyncio


async def main():
    await asyncio.sleep(1)
    return "Hello"

loop = asyncio.get_event_loop()
future = asyncio.ensure_future(main())

loop.run_until_complete(future)
print("Result:", future.result())
