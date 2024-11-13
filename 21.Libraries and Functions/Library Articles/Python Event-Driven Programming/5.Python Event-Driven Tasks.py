import asyncio

async def foo():
    print("Foo")
    await asyncio.sleep(1)
    print("End Foo")

async def bar():
    print("Bar")
    await asyncio.sleep(2)
    print("End Bar")

loop = asyncio.get_event_loop()
task1 = loop.create_task(foo())
task2 = loop.create_task(bar())

loop.run_until_complete(asyncio.wait([task1, task2]))
