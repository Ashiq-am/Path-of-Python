# Python3 code to demonstrate working of
# Extract K length substrings
# Using itertools.combinations()
from itertools import combinations

# initializing string
test_str = "Geeks"

# printing original string
print("The original string is : " + str(test_str))

# initializing K
K = 3

# Extract K length substrings
# Using itertools.combinations()
res = [test_str[x:y] for x, y in combinations(range(len(test_str) + 1), r = 2) if len(test_str[x:y]) == K ]

# printing result
print("All K length substrings of string are : " + str(res))
