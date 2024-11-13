# Python3 program to Merge two list of
# lists according to first element
import collections


def merge(lst1, lst2):
    return [(sub + [lst2[i][-1]]) for i, sub in enumerate(lst1)]


# Driver code
lst1 = [[1, 'Alice'], [2, 'Bob'], [3, 'Cara']]
lst2 = [[1, 'Delhi'], [2, 'Mumbai'], [3, 'Chennai']]
print(merge(lst1, lst2))
