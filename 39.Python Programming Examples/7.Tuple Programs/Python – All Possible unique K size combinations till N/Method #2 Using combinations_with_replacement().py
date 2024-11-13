# Python3 code to demonstrate working of
# All Possible unique K size combinations till N
# Using combinations_with_replacement()
from itertools import product, combinations_with_replacement

# initializing N
N = 4

# Initialize K
K = 3

# All Possible unique K size combinations till N
# Using combinations_with_replacement()
res = list(combinations_with_replacement(range(N), K))

# printing result
print("The unique combinations : " + str(res))
