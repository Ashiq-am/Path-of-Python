# Python3 code to demonstrate working of
# Pair Product combinations
# Using list comprehension + zip() + operator.mul + combinations()
from itertools import combinations
import operator

# initialize list
test_list = [(2, 4), (6, 7), (5, 1), (6, 10)]

# printing original list
print("The original list : " + str(test_list))

# Pair Product combinations
# Using list comprehension + zip() + operator.mul + combinations()
res = [(operator.mul(*a), operator.mul(*b))\
	for a, b in (zip(y, x) for x, y in combinations(test_list, 2))]

# printing result
print("The Product pair combinations are : " + str(res))
