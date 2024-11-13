# Python3 program to ways to convert
# list enclosed within string to list
from ast import literal_eval


def convert(lst):
    return literal_eval(lst)


# Driver code
lst = "[0, 2, 9, 4, 8]"
print(convert(lst))
