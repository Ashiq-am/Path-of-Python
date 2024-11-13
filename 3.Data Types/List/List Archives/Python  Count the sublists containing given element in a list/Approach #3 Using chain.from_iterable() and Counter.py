# Python3 Program to count number of
# list containing a certain element
# in a list of lists
from itertools import chain
from collections import Counter


def countList(lst, x):
    return Counter(chain.from_iterable(set(i) for i in lst))[x]


# Driver Code
lst = (['a'], ['a', 'c', 'b'], ['d'])
x = 'a'
print(countList(lst, x))
