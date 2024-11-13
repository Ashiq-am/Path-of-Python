# Python3 program to Find all combinations
# of string after deleting k characters
from itertools import combinations


def findCombinations(str, k):
    l = len(str)
    return set([''.join(i) for i in combinations(str, l - k)])


# Driver Code
str = 'geeks'
k = 1
print(findCombinations(str, k))
