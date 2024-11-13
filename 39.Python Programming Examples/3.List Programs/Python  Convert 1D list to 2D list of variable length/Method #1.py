# Python3 program to Convert 1D
# list to 2D list
from itertools import islice


def convert(lst, var_lst):
    idx = 0
    for var_len in var_lst:
        yield lst[idx: idx + var_len]
        idx += var_len


# Driver code
lst = [1, 2, 3, 4, 5, 6]
var_lst = [1, 2, 3]
print(list(convert(lst, var_lst)))
