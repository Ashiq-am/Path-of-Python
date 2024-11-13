import asyncio


async def function_asyc():
    i = 0
    while i < 1000000:
        i += 1
        if i % 50000 == 0:
            print("Hello, I'm Abhishek")
            print("GFG is Great")
            await asyncio.sleep(0.01)


async def function_2():
    print("\n HELLO WORLD \n")


async def main():
    # New Line Added
    while True:
        f1 = loop.create_task(function_asyc())
        f2 = loop.create_task(function_2())
        await asyncio.wait([f1, f2])


# to run the above function we'll
# use Event Loops these are low
# level functions to run async functions
loop = asyncio.get_event_loop()
loop.run_until_complete(main())
loop.close()
