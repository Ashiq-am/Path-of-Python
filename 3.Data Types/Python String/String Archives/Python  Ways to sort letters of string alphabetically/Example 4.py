# Python3 program to sort letters
# of string alphabetically
from itertools import accumulate


def sortString(str):
    return "".join(sorted(str, key=lambda x: x.lower()))


# Driver code
str = 'Geeks'
print(sortString(str))
