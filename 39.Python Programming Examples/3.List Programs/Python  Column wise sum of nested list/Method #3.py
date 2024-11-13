# Python3 program to Column wise sum of nested list
from numpy import array


def column_sum(lst):
    arr = array(lst)
    return sum(arr, 0).tolist()


# Driver code
lst = [[1, 5, 3], [2, 7, 8], [4, 6, 9]]
print(column_sum(lst))
