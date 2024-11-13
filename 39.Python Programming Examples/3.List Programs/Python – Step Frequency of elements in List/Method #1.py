# Python3 code to demonstrate
# Step Frequency of elements in List
# using loop + defaultdict()
from collections import defaultdict

# Initializing loop
test_list = ['gfg', 'is', 'best', 'gfg', 'is', 'life']

# printing original list
print("The original list is : " + str(test_list))

# Step Frequency of elements in List
# using loop + defaultdict()
res_d = defaultdict(int)
res = []
for ele in test_list:
	res_d[ele] += 1
	res.append(res_d[ele])

# printing result
print ("Step frequency of elements is : " + str(res))
