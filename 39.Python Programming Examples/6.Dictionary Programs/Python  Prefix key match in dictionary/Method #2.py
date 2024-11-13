# Python3 code to demonstrate working of
# Prefix key match in dictionary
# Using map() + filter() + items() + startswith()

# Initialize dictionary
test_dict = {'tough' : 1, 'to' : 2, 'do' : 3, 'todays' : 4, 'work' : 5}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# Initialize prefix
test_pref = 'to'

# Using map() + filter() + items() + startswith()
# Prefix key match in dictionary
res = dict(filter(lambda item: item[0].startswith(test_pref),
										test_dict.items()))

# printing result
print("Filtered dictionary keys are : " + str(res))
