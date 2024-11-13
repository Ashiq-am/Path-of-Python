# Python3 program to sort letters
# of string alphabetically
from itertools import accumulate


def sortString(str):
    return tuple(accumulate(sorted(str)))[-1]


# Driver code
str = 'PYTHON'
print(sortString(str))
