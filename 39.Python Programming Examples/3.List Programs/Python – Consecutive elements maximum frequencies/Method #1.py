# Python3 code to demonstrate working of
# Consecutive elements maximum frequencies
# Using loop + groupby()
from itertools import groupby

# initializing list
test_list = [5, 6, 7, 7, 6, 6, 5, 7]

# printing original list
print("The original list is : " + str(test_list))

# Consecutive elements maximum frequencies
# Using loop + groupby()
res = {}
for key, val in groupby(test_list):
	sub = sum(1 for _ in val)
	if res.get(key, float('-inf')) < sub:
		res[key] = sub

# printing result
print("The maximum frequencies : " + str(res))
