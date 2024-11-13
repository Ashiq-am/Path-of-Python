# Python3 code to demonstrate working of
# Convert list of tuples to dictionary value lists
# Using defaultdict() + loop
from collections import defaultdict

# initializing list
test_list = [(1, 'gfg'), (1, 'is'), (2, 'best'), (3, 'for'), (4, 'CS')]

# printing original list
print("The original list is : " + str(test_list))

# Using defaultdict() + loop
# Convert list of tuples to dictionary value lists
res = defaultdict(list)
for i, j in test_list:
	res[i].append(j)

# printing result
print("The merged dictionary is : " + str(dict(res)))
