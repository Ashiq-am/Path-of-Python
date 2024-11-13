# Python program to find the
# frequency of largest element

import collections

L = [1, 2, 8, 5, 8, 7, 8]

# find the largest element
largest = max(L)

# Storing the occurrences of each
# element of list in res
res = collections.Counter(L)

print(res[largest])
