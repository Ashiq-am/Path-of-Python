# Python3 code to demonstrate working of
# Retain K consecutive elements
# using groupby() + list comprehension
from itertools import groupby

# initialize list
test_list = [1, 1, 4, 5, 5, 6, 7, 7, 8]

# printing original list
print("The original list : " + str(test_list))

# initialize K
K = 2

# Retain K consecutive elements
# using groupby() + list comprehension
res = [i for i, j in groupby(test_list) if len(list(j)) == K]

# printing result
print("The K consecutive elements are : " + str(res))
