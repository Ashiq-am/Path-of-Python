# Python3 code to demonstrate working of
# Maximum N repeated Elements
# Using Counter() + loop
from collections import Counter

# initializing list
test_list = [5, 7, 7, 2, 5, 5, 7, 2, 2]

# printing original list
print("The original list : " + str(test_list))

# initializing N
N = 2

# Using Counter() + loop
res = []
temp = Counter(test_list)
for key, ele in temp.items():

	# Conditional check for size decision during append
	if ele <= N:
		res.extend([key for idx in range(ele)])
	else:
		res.extend([key for idx in range(N)])

# printing result
print("Extracted elements : " + str(res))
