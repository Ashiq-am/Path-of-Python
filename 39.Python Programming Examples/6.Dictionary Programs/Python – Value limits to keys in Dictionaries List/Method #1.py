# Python3 code to demonstrate working of
# Value limits to keys in Dictionaries List
# Using max() + min() + loop + keys()

# initializing Matrix
test_list = [{"gfg": 4, "is": 7, "best": 10},
			{"gfg": 2, "is": 5, "best": 9},
			{"gfg": 1, "is": 2, "best": 6}]

# printing original list
print("The original list is : " + str(test_list))

res = dict()

# extraction of all keys
keys = list(test_list[0].keys())

for key in keys:

	# assigning ranges to each key
	res[key] = [min(sub[key] for sub in test_list), max(sub[key]
														for sub in test_list)]

# printing result
print("Keys Ranges : " + str(res))
