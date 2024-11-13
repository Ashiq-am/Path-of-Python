# Python3 code to demonstrate working of
# Merge keys by values
# Using defaultdict() + loop
from collections import defaultdict

# initializing dictionary
test_dict = {1: 6, 8: 1, 9: 3, 10: 3, 12: 6, 4: 9, 2: 3}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# grouping values
temp = defaultdict(list)
for key, val in sorted(test_dict.items()):
	temp[val].append(key)

res = dict()
# merge keys
for key in temp:
	res['-'.join([str(ele) for ele in temp[key]])] = key

# printing result
print("The required result : " + str(res))
