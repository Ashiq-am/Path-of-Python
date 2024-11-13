# Python3 program to Merge two list of
# lists according to first element
import collections


def merge(lst1, lst2):
    dict1 = collections.defaultdict(list)

    for e in lst1 + lst2:
        dict1[e[0]].append(e[1])
    dictlist = list()

    for key, value in dict1.items():
        dictlist.append([key] + value)

    return dictlist


# Driver code
lst1 = [[1, 'Alice'], [2, 'Bob'], [3, 'Cara']]
lst2 = [[1, 'Delhi'], [2, 'Mumbai'], [3, 'Chennai']]
print(merge(lst1, lst2))
