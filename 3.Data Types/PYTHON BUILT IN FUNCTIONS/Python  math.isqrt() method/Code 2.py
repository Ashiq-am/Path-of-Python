# Python Program to explain
# math.isqrt() method


import math


def isPerfect(n):
    # Get the floor value of
    # exact square root of n
    sqrt = math.isqrt(n)

    if sqrt * sqrt == n:
        print(f"{n} is perfect square")

    else:
        print(f"{n} is not a perfect square")


# Driver's code
isPerfect(100)
isPerfect(10)
