# Python3 code to demonstrate working of
# All possible N combination tuples
# Using product()
from itertools import product

# initialize N
N = 3

# All possible N combination tuples
# Using product()
res = list(product(range(1, N + 1), repeat = N))

# printing result
print("Tuple Combinations till N are : " + str(res))
