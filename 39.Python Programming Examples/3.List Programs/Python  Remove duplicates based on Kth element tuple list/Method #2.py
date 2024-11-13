# Python3 code to demonstrate working of
# Remove duplicates based on Kth element tuple list
# Using reduce() + lambda + keys()
from functools import reduce

# initialize list
test_list = [(3, 1), (1, 3), (3, 2), (5, 2), (5, 3)]

# printing original list
print("The original list is : " + str(test_list))

# initialize K
K = 0

# Remove duplicates based on Kth element tuple list
# Using reduce() + lambda + keys()
res = reduce(lambda sub, ele : ele[K] in dict(sub).keys()
				and sub or sub + [ele], test_list, [])

# printing result
print("The list after removal of K based duplicates : " + str(res))
