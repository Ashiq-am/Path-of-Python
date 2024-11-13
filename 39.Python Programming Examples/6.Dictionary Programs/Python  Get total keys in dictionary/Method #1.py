# Python3 code to demonstrate working of
# Get total keys in dictionary
# Using recursion + items() + sum() + len()

# Utility function to perform task
def total_keys(test_dict):
	return (0 if not isinstance(test_dict, dict)
	else len(test_dict) + sum(total_keys(val) for val in test_dict.values()))

# Initialize dictionary
test_dict = { 'gfg' : { 'is' : 1, 'best' : { 'for' : {'geeks' :4}}}}

# Printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Using recursion + items() + sum() + len()
# Get total keys in dictionary
res = total_keys(test_dict)

# printing result
print("Number of keys in dictionary is : " + str(res))
