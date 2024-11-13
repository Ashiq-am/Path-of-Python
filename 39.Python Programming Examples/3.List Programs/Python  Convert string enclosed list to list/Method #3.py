# Python3 program to ways to convert
# list enclosed within string to list
from json import loads


def convert(lst):
    return loads(lst)


# Driver code
lst = "[0, 2, 9, 4, 8]"
print(convert(lst))
