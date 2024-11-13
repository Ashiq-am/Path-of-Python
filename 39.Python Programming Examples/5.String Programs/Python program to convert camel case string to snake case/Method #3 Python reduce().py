# Python3 program to convert string
# from camel case to snake case
from functools import reduce


def change_case(str):
    return reduce(lambda x, y: x + ('_' if y.isupper() else '') + y, str).lower()


# Driver code
str = "GeeksForGeeks"
print(change_case(str))
