import asyncio


async def square_number(n):
    for i in range(1, n + 1):
        print("Square of ", i, "is ", i ** 2)
        await asyncio.sleep(0.001)


async def square_root(n):
    print("Square root of ", n, " rounded to nearest integer is ",
          round(n ** .5))


async def divide(num1, num2):
    if num2 == 0:
        raise Exception("Trying to Divide by Zero")
    else:
        print(num1 / num2)


async def main():
    tasks = asyncio.gather(square_number(5),
                           square_root(16),
                           divide(15, 0),
                           square_root("Geek"))

    await tasks


asyncio.run(main())
