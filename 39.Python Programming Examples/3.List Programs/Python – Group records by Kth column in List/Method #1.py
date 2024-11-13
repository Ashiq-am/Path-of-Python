# Python3 code to demonstrate
# Group records by Kth column in List
# using loop + defaultdict()
from collections import defaultdict

# Initializing list
test_list = [('Gfg', 1), ('is', 2), ('Gfg', 3), ('is', 4), ('best', 5)]

# printing original list
print("The original list is : " + str(test_list))

# Initializing K
K = 0

# Group records by Kth column in List
# using loop + defaultdict()
temp = defaultdict(list)
for ele in test_list:
	temp[ele[K]].append(ele)
res = list(temp.values())

# printing result
print ("The list after grouping : " + str(res))
