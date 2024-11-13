# Python code to demonstrate
# Nested List Intersection Matrix Product
# using reduce() + lambda + set() + loop

# getting Product
from functools import reduce


def prod(val) :
	res = 1
	for ele in val:
		res *= ele
	return res

# initializing list of lists
test_list = [[2, 3, 5, 8], [2, 6, 7, 3], [10, 9, 2, 3]]

# printing original list
print ("The original list is : " + str(test_list))

# Nested List Intersection Matrix Product
# using reduce() + lambda + set() + loop
res = prod(list(reduce(lambda i, j: i & j, (set(x) for x in test_list))))

# printing result
print ("The common row elements product is : " + str(res))
