# Python3 code to demonstrate working of
# Initialize dictionary with multiple keys
# Using loop

# declare dictionary
test_dict = {}

# printing original dictionary
print("The original dictionary : " + str(test_dict))

# Initialize keys
test_keys = ['gfg', 'is', 'best']

# Using loop
# Initialize dictionary with multiple keys
for keys in test_keys:
	test_dict[keys] = 4

# printing result
print("Dictionary after updating multiple key-value : " + str(test_dict))
