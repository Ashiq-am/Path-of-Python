# Python program to merge two 3D list into one
# importing pretty printed
import pprint


def ThreeD(a, b, c):
    lst1 = [[['1' for col in range(a)] for col in range(b)] for row in range(c)]
    lst2 = [[['2' for col in range(a)] for col in range(b)] for row in range(c)]
    # Merging using "+" operator
    lst = lst1 + lst2
    return lst


# Driver Code
col1 = 3
col2 = 3
row = 3

# used the pretty printed function
pprint.pprint(ThreeD(col1, col2, row))
