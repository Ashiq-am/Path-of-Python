# Python3 code to demonstrate working of
# Maximum of Similar Keys in Tuples
# Using max() + groupby() + lambda + loop
from itertools import groupby

# initializing lists
test_list = [(4, 8), (3, 2), (2, 2), (4, 6), (3, 7), (4, 5)]

# printing original list
print("The original list is : " + str(test_list))

# Maximum of Similar Keys in Tuples
# Using max() + groupby() + lambda + loop
test_list.sort(key = lambda sub: sub[0])
temp = groupby(test_list, lambda ele: ele[0])
res = []
for key, val in temp:
	res.append((key, sum([ele[1] for ele in val])))

# printing result
print("Maximum grouped elements : " + str(res))
