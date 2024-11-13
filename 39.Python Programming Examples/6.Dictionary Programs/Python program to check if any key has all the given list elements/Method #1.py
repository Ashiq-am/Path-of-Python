# Python3 code to demonstrate working of
# Extract values of Particular Key in
# Nested Values Using list comprehension

# initializing dictionary
test_dict = {'Gfg': [5, 3, 1, 6, 4],
			'is': [8, 2, 1, 6, 4],
			'best': [1, 2, 7, 3, 9],
			'for': [5, 2, 7, 8, 4, 1],
			'all': [8, 5, 3, 1, 2]}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# initializing list
find_list = [7, 9, 2]

res = False
for key in test_dict:

	# checking if all values present using
	# superset
	if set(test_dict[key]).issuperset(find_list):
		res = True

# printing result
print("Is any value list superset ? : " + str(res))
