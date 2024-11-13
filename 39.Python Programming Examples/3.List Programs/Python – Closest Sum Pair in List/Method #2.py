# Python3 code to demonstrate
# Closest Sum Pair in List
# using loop + combinations
from itertools import combinations

# Initializing list
test_list = [7, 8, 10, 3, 18, 1]

# printing original list
print("The original list is : " + str(test_list))

# Initializing K
K = 12

# Closest Sum Pair in List
# using dictionary comprehension + max()
res = {}
for ele in combinations(test_list, 2):
	ele_sum = sum(ele)
	try:
		res[ele_sum].append(ele)
	except KeyError:
		res[ele_sum] = [ele]
res = res[min(res, key = lambda ele: abs(ele - K))]

# printing result
print ("The closest sum pair is : " + str(res))
