import asyncio

async def long_running_task():
    await asyncio.sleep(5)

async def main():
    try:
        await asyncio.wait_for(long_running_task(), timeout=2)
        print("Task completed successfully.")
    except asyncio.TimeoutError:
        print("The task took too long and timed out.")

asyncio.run(main())
