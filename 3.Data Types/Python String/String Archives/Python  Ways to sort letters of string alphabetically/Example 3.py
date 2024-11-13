# Python3 program to sort letters
# of string alphabetically
from functools import reduce


def sortString(str):
    return reduce(lambda a, b: a + b, sorted(str))


# Driver code
str = 'PYTHON'
print(sortString(str))
