# Python3 program to find most common
# element in each column in a 2D list
from collections import Counter


def mostCommon(lst):
    return [Counter(col).most_common(1)[0][0] for col in zip(*lst)]


# Driver code
lst = [[1, 1, 3],
       [2, 3, 3],
       [3, 2, 2],
       [2, 1, 3]]
print(mostCommon(lst))
