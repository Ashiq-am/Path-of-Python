# Python3 code to demonstrate working of
# Grouping list values into dictionary
# Using defaultdict() + loop + dict()
from collections import defaultdict

# initializing list
test_list = [['Gfg', 1], ['Gfg', 2], ['is', 3], ['best', 4], ['is', 5]]

# printing original list
print("The original list is : " + str(test_list))

# Grouping list values into dictionary
# Using defaultdict() + loop + dict()
temp = defaultdict(list)
for key, val in test_list:
	temp[key].append(val)
res = dict((key, tuple(val)) for key, val in temp.items())

# printing result
print("The grouped dictionary is : " + str(res))
