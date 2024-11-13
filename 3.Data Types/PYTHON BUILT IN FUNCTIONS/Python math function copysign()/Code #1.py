# Python code to demonstrate copy.sign() function
import math


def func():
    a = 5
    b = -7

    # implementation of copysign
    c = math.copysign(a, b)

    return c

print(func())
