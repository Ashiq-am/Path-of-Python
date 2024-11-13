# Python3 program to Convert 1D
# list to 2D list
from itertools import islice


def convert(lst, var_lst):
    it = iter(lst)
    return [list(islice(it, i)) for i in var_lst]


# Driver code
lst = [1, 2, 3, 4, 5, 6]
var_lst = [1, 2, 3]
print(convert(lst, var_lst))
