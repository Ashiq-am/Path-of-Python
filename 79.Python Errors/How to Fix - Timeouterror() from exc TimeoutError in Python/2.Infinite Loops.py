import asyncio

async def my_task():
    while True:
        await asyncio.sleep(1)  # Infinite loop, simulating ongoing task

async def main():
    await asyncio.wait_for(my_task(), timeout=2)

asyncio.run(main())
