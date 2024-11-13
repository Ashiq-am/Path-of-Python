import asyncio

async def my_task():
    await asyncio.sleep(3)  # Simulate some long-running operation
    return "Task completed"

async def main():
    result = await asyncio.wait_for(my_task(), timeout=2)
    print(result)

asyncio.run(main())
