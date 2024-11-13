# Python Program to Print
# all subsets of given size of a set

import itertools


# def findsubsets(s, n):
def findsubsets(s, n):
    return [set(i) for i in itertools.combinations(s, n)]


# Driver Code
s = {1, 2, 3, 4}
n = 3

print(findsubsets(s, n))
