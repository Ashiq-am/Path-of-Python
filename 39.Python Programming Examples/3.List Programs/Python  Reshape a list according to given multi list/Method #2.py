# Python3 program to reshape a list
# according to multidimensional list
from itertools import islice


def yieldSublist(lst1, lst2):
    iter2 = iter(lst2)
    for sublist1 in lst1:
        sublist2 = list(islice(iter2, len(sublist1)))
        yield sublist2


def reshape(lst1, lst2):
    res = list()
    for sub2 in yieldSublist(list1, list2):
        res.append(sub2)

    return res


# Driver code
list1 = [[1], [2, 3], [4, 5, 6]]
list2 = ['a', 'b', 'c', 'd', 'e', 'f']
print(reshape(list1, list2))
