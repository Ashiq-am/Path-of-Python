# Python3 code to demonstrate working of
# Prefix key match in dictionary
# Using dictionary comprehension + startswith()

# Initialize dictionary
test_dict = {'tough' : 1, 'to' : 2, 'do' : 3, 'todays' : 4, 'work' : 5}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# Initialize prefix
test_pref = 'to'

# Using dictionary comprehension + startswith()
# Prefix key match in dictionary
res = {key:val for key, val in test_dict.items()
				if key.startswith(test_pref)}

# printing result
print("Filtered dictionary keys are : " + str(res))
