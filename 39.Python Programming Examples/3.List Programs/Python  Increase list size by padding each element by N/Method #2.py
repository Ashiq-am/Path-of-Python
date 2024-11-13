# Python3 program to increase list size
# by padding each element by N
from functools import reduce


def increaseSize(lst, N):
    return reduce(lambda x, y: x + y, [[el] * N for el in lst])


# Driver code
lst = [1, 2, 3]
N = 3
print(increaseSize(lst, N))
