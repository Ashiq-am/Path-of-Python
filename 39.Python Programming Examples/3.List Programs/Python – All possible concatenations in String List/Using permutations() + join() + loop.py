# Python3 code to demonstrate working of
# All possible concatenations in String List
# Using permutations() + loop
from itertools import permutations

# initializing list
test_list = ['Gfg', 'is', 'Best']

# printing original list
print("The original list : " + str(test_list))

# All possible concatenations in String List
# Using permutations() + loop
temp = []
for idx in range(1, len(test_list) + 1):
	temp.extend(list(permutations(test_list, idx)))
res = []
for ele in temp:
	res.append("".join(ele))

# printing result
print("All Sring combinations : " + str(res))
