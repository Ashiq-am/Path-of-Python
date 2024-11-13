# Python3 code to demonstrate working of
# List of N size increasing lists
# Using combinations()
from itertools import combinations

# initializing N
N = 2

# initializing M
M = 4

# using combinations to perform task
res = list(combinations(list(range(1, M + 1)), N))

# printing result
print("The constructed combinations : " + str(res))
