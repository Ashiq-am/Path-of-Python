# Python3 code to demonstrate working of
# All elements difference in Set
# Using combinations + abs() + loop
from itertools import combinations

# initializing strings set
test_set = {1, 5, 2, 7, 3, 4, 10, 14}

# printing original string
print("The original set is : " + str(test_set))

# getting combinations
combos = combinations(test_set, 2)

res = set()

# adding differences in set
for x, y in combos:
	res.add(abs(x - y))

# printing result
print("All possible differences : " + str(res))
