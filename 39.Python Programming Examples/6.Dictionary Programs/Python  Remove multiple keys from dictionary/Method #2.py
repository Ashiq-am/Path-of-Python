# Python3 code to demonstrate working of
# Remove multiple keys from dictionary
# Using items() + list comprehension + dict()

# initializing dictionary
test_dict = {'Gfg' : 1, 'is' : 2, 'best' : 3, 'for' : 4, 'CS' : 5}

# initializing Remove keys
rem_list = ['is', 'for', 'CS']

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Using items() + list comprehension + dict()
# Remove multiple keys from dictionary
res = dict([(key, val) for key, val in
		test_dict.items() if key not in rem_list])

# printing result
print("Dictionary after removal of keys : " + str(res))
