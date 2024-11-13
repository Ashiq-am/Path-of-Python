# Python3 code to demonstrate working of
# Size Range Combinations in list
# Using loop + extend() + combinations()
from itertools import combinations

# initializing list
test_list = [4, 5, 6, 7, 3, 8]

# printing original list
print("The original list is : " + str(test_list))

# initializing i, j
i, j = 2, 4

# Size Range Combinations in list
# Using loop + extend() + combinations()
res = []
for sub in range(j):
	if sub >= (i - 1):
		res.extend(combinations(test_list, sub + 1))

# Printing result
print("The combinations of elements in range of i and j : " + str(res))
