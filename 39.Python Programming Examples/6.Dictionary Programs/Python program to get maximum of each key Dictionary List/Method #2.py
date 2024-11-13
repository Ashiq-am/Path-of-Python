# Python3 code to demonstrate working of
# All Keys Maximum in Dictionary List
# Using defaultdict()
from collections import defaultdict

# initializing Matrix
test_list = [{"Gfg": 8, "is": 1, "Best": 9},
			{"Gfg": 2, "is": 9, "Best": 1},
			{"Gfg": 5, "is": 10, "Best": 7}]

# printing original list
print("The original list is : " + str(test_list))


res = defaultdict(int)
for dic in test_list:
	for key, val in dic.items():

		# defaultdict helps to avoid conditional check here
		res[key] = max(res[key], val)

# printing result
print("All keys maximum : " + str(dict(res)))
