# Python3 program to increase list size
# by padding each element by N
from itertools import chain


def increaseSize(lst, N):
    return list(chain(*([el] * N for el in lst)))


# Driver code
lst = [1, 2, 3]
N = 3
print(increaseSize(lst, N))
