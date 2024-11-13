# Python3 Program to count occurrence
# of all elements of list in a tuple
from collections import Counter


def countOccurrence(tup, lst):
    count = 0
    for item in tup:
        if item in lst:
            count += 1

    return count


# Driver Code
tup = ('a', 'a', 'c', 'b', 'd')
lst = ['a', 'b']
print(countOccurrence(tup, lst))
