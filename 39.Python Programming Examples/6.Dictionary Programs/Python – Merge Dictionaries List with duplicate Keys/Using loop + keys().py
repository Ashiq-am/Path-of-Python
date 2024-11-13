# Python3 code to demonstrate working of
# Merge Dictionaries List with duplicate Keys
# Using loop + keys()

# initializing lists
test_list1 = [{"gfg": 1, "best": 4}, {"geeks": 10, "good": 15},
			{"love": "gfg"}]

test_list2 = [{"gfg": 6}, {"better": 3, "for": 10, "geeks": 1},
			{"gfg": 10}]

# printing original lists
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))


for idx in range(0, len(test_list1)):

	# getting keys of corresponding index
	id_keys = list(test_list1[idx].keys())
	for key in test_list2[idx]:

		# checking for keys presence
		if key not in id_keys:
			test_list1[idx][key] = test_list2[idx][key]

# printing result
print("The Merged Dictionary list : " + str(test_list1))
