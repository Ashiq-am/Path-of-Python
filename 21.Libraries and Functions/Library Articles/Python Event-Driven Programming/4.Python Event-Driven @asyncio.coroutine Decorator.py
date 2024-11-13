import asyncio


@asyncio.coroutine
def countdown(n):
    while n > 0:
        print("T-minus", n)
        yield from asyncio.sleep(1)
        n -= 1


loop = asyncio.get_event_loop()
loop.run_until_complete(countdown(3))
