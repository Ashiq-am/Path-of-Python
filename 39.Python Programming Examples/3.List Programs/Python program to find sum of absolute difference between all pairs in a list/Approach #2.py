# Python3 program to find sum of
# absolutre differences in all pairs
import itertools


def sumPairs(lst):
    diffs = [abs(e[1] - e[0]) for e in itertools.permutations(lst, 2)]
    return int(sum(diffs) / 2)


# Driver program
lst = [9, 8, 1, 16, 15]
print(sumPairs(lst))
