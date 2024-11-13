import asyncio

async def greet(name):
    print("Hello", name)
    await asyncio.sleep(1)
    print("Goodbye", name)

loop = asyncio.get_event_loop()
loop.run_until_complete(greet("Alice"))
