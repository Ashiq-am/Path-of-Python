# Python3 code to demonstrate working of
# Finding min value keys in dictionary
# Using all() + list comprehension

# initializing dictionary
test_dict = {'Gfg' : 1, 'for' : 2, 'CS' : 1}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Using all() + list comprehension
# Finding min value keys in dictionary
res = [key for key in test_dict if
		all(test_dict[temp] >= test_dict[key]
		for temp in test_dict)]

# printing result
print("Keys with minimum values are : " + str(res))
