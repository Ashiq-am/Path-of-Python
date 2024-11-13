# Python3 Program to count occurrence
# of all elements of list in a tuple
from collections import Counter


def countOccurrence(tup, lst):
    counts = Counter(tup)
    return sum(counts[i] for i in lst)


# Driver Code
tup = ('a', 'a', 'c', 'b', 'd')
lst = ['a', 'b']
print(countOccurrence(tup, lst))
