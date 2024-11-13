def find_depth(ele, dicti):

	# finding depth
	for idx in range(len(list(dicti.keys()))):

		# assigning value as key if found
		if ele in list(dicti.keys()):
			ele = dicti[ele]
	return ele


# initializing dictionary
test_dict = {3: 4, 5: 6, 4: 8, 6: 9, 8: 10}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

res = dict()

# iterating for each key
for key, val in list(test_dict.items()):
	test_dict.pop(key)
	res[key] = find_depth(val, test_dict)

# printing result
print("The reassigned dictionary : " + str(res))
