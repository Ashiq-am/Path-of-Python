# Python3 code to demonstrate working of
# Group Elements in Matrix
# Using loop + defaultdict()
from collections import defaultdict

# initializing list
test_list = [[5, 8], [2, 0], [5, 4], [2, 3], [7, 9]]

# printing original list
print("The original list : " + str(test_list))

# initializing empty dictionary using defaultdict
res = defaultdict(list)

# using loop for grouping
for idx in test_list:
	res[idx[0]].append(idx[1])

# printing result
print("The Grouped Matrix : " + str(dict(res)))
