# Python3 code to demonstrate working of
# Get specific keys' values
# Using map() + get()

# initializing dictionary
test_dict = {'gfg' : 1, 'is' : 2, 'best' : 3}

# initializing keys
filt_keys = ['gfg', 'best']

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Extract specific value list from dictionary
# Using map() + get()
res = list(map(test_dict.get, filt_keys))

# printing result
print("Filtered value list is : " + str(res))
