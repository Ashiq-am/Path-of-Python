from itertools import starmap
from operator import mul

# function to perform task
def tup_prod(tup1, tup2):
	return tuple(starmap(mul, zip(tup1, tup2)))

# initialize tuples
test_tup1 = ((1, 3), (4, 5), (2, 9), (1, 10))
test_tup2 = ((6, 7), (3, 9), (1, 1), (7, 3))

# printing original tuples
print("The original tuple 1 : " + str(test_tup1))
print("The original tuple 2 : " + str(test_tup2))

# Cumulative Nested Tuple Column Product
# using itertools and starmap
res = tuple(starmap(tup_prod, zip(test_tup1, test_tup2)))

# printing result
print("The resultant tuple after product : " + str(res))
#This code is contrinuted by Pushpa.
