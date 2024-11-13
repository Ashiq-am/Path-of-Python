# Python3 code to demonstrate working of
# Multiple Sets Intersection
# Using reduce() + and_ operator
from operator import and_
from functools import reduce

# initializing list
test_list = [{5, 3, 6, 7}, {1, 3, 5, 2}, {7, 3, 8, 5}, {8, 4, 5, 3}]

# printing original list
print("The original list is : " + str(test_list))

# getting all sets intersection using and_ operator
res = set(reduce(and_, test_list))

# printing result
print("Intersected Sets : " + str(res))
