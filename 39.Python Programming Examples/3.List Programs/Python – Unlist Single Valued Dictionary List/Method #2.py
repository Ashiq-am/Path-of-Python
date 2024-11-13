# Python3 code to demonstrate working of
# Unlist Single Valued Dictionary List
# Using list comprehension + isinstance()

# initializing list
test_list = [{'Gfg': 1,
			'is': [{'a': 2, 'b': 3}]},
			{'best': [{'c': 4, 'd': 5}],
			'CS': 6}]

# printing original list
print("The original list is : " + str(test_list))

# Using list comprehension + isinstance()
# Similar way as above, extrating first element of list
res = [{key: val[0] if isinstance(val, list) else val
		for key, val in sub.items()}
		for sub in test_list]

# printing result
print("The converted Dictionary list : " + str(res))
