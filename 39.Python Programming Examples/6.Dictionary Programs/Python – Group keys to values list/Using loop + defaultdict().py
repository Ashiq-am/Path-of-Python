# Python3 code to demonstrate working of
# Group keys to values list
# Using loop + defaultdict()
from collections import defaultdict

# initializing list
test_list = [{'gfg' : 1, 'is' : 4, 'best' : 7},
			{'gfg' : 9, 'is' : 8, 'best' : 3},
			{'gfg' : 4, 'is' : 4, 'best' : 7},
			{'gfg' : 7, 'is' : 2, 'best' : 8},
			{'gfg' : 1, 'is' : 4, 'best' : 7},
			{'gfg' : 10, 'is' : 9, 'best' : 2},
			{'gfg' : 0, 'is' : 5, 'best' : 6}]

# printing original list
print("The original list is : " + str(test_list))

# Group keys to values list
# Using loop + defaultdict()
res = defaultdict(set)
for sub in test_list:
	for key, val in sub.items():
		res[key].add(val)

# printing result
print("The grouped key values : " + str(dict(res)))
