# Python3 program to Find total number
# of triplets in a list with given sum
from itertools import combinations


def findTriplets(lst, key):
    def valid(val):
        return sum(val) == key

    return list(filter(valid, list(combinations(lst, 3))))


# Driver Code
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(findTriplets(lst, 10))
