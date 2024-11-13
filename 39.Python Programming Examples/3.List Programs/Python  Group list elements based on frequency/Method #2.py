# Python3 program to Grouping list
# elements based on frequency
from collections import Counter


def group_list(lst):
    return list(zip(Counter(lst).keys(), Counter(lst).values()))


# Driver code
lst = [1, 3, 4, 4, 1, 5, 3, 1]
print(group_list(lst))
