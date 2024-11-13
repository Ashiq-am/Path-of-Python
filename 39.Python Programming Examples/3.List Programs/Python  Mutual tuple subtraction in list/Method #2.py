# Python3 code to demonstrate working of
# Mutual tuple subtraction in list
# Using list comprehension + zip() + operator.sub + combinations()
from itertools import combinations
import operator

# initialize list
test_list = [(2, 4), (6, 7), (5, 1), (6, 10)]

# printing original list
print("The original list : " + str(test_list))

# Mutual tuple subtraction in list
# Using list comprehension + zip() + operator.sub + combinations()
res = [(operator.sub(*a), operator.sub(*b))\
	for a, b in (zip(y, x) for x, y in combinations(test_list, 2))]

# printing result
print("The mutual subtraction tuples are : " + str(res))
