# Python3 code to demonstrate working of
# Check for Non None Dictionary values
# Using all() + not operator + values()

# initializing dictionary
test_dict = {'Gfg' : 1, 'for' : 2, 'CS' : None}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# Using all() + not operator + values()
# Check for Non None Dictionary values
res = not all(test_dict.values())

# printing result
print("Does Dictionary contain None value ? " + str(res))
