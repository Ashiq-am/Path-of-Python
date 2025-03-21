# Python3 program to Remove elements of
# list that repeated less than k times
from collections import Counter


def removeElements(lst, k):
    counted = Counter(lst)

    temp_lst = []
    for el in counted:
        if counted[el] < k:
            temp_lst.append(el)

    res_lst = []
    for el in lst:
        if el not in temp_lst:
            res_lst.append(el)

    return (res_lst)


# Driver code
lst = ['a', 'a', 'a', 'b', 'b', 'c']
k = 2
print(removeElements(lst, k))
