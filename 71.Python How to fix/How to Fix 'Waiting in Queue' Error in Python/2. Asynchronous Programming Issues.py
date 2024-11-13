import asyncio
import random

async def worker(name, queue):
    while True:
        item = await queue.get()
        if item is None:
            break
        print(f'{name} processing item: {item}')
        await asyncio.sleep(random.uniform(0.5, 1.5))
        queue.task_done()
async def main():
    queue = asyncio.Queue()
    workers = [asyncio.create_task(worker(f'worker-{i}', queue)) for i in range(5)]
    for item in range(20):
        await queue.put(item)
    await queue.join()

    for _ in range(5):
        await queue.put(None)
    await asyncio.gather(*workers)
asyncio.run(main())
