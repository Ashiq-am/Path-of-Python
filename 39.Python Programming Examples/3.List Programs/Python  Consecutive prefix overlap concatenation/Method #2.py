# Python3 code to demonstrate working of
# Consecutive prefix overlap concatenation
# Using reduce() + lambda + next()

# initializing list
from functools import reduce

test_list = ["gfgo", "gone", "new", "best"]

# printing original list
print("The original list is : " + str(test_list))

# Consecutive prefix overlap concatenation
# Using reduce() + lambda + next()
res = reduce(lambda i, j: i + j[next(idx
			for idx in reversed(range(len(j) + 1))
			if i.endswith(j[:idx])):], test_list, '', )

# printing result
print("The resultant joined string : " + str(res))
