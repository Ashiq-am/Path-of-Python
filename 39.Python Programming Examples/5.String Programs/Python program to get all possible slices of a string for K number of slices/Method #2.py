# Python3 code to demonstrate working of
# All possible slices for K length
# Using combinations() + zip() + list comprehension
from itertools import combinations

# initializing string
test_str = "Gfg4all"

# printing original string
print("The original string is : " + str(test_str))

# initializing number of slices
K = 3

# combinations used to perform all possible slices
res = [[test_str[idx: j] for idx, j in zip([None, *sub], [*sub, None])]
	for sub in combinations(range(1, len(test_str)), K - 1)]

# printing result
print("All possible slices for K strings : " + str(res))
