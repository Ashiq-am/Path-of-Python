# Python program to print 3D list
# importing pretty printed
import pprint


def ThreeD(a, b, c):
    lst = [[['#' for col in range(a)] for col in range(b)] for row in range(c)]
    return lst


# Driver Code
col1 = 5
col2 = 3
row = 2
# used the pretty printed function
pprint.pprint(ThreeD(col1, col2, row))
