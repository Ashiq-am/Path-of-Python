import asyncio

async def long_running_task():
    await asyncio.sleep(5)

async def main():
    try:
        result = await asyncio.wait_for(long_running_task(), timeout=2)
        print("Task completed:", result)
    except asyncio.TimeoutError:
        print("Task timed out!")

asyncio.run(main())
