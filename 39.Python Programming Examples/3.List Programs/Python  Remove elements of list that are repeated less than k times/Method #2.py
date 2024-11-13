# Python3 program to Remove elements of
# list that repeated less than k times
from collections import Counter


def removeElements(lst, k):
    counted = Counter(lst)
    return [el for el in lst if counted[el] >= k]


# Driver code
lst = ['a', 'a', 'a', 'b', 'b', 'c']
k = 2
print(removeElements(lst, k))
