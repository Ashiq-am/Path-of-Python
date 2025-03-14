# Python3 code to demonstrate working of
# Check for Key in Dictionary Value list
# Using list comprehension + in operator

# initializing dictionary
test_dict = {'Gfg': [{'CS': 5}, {'GATE': 6}], 'for': 2, 'CS': 3}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# initializing key
key = "GATE"

# Check for Key in Dictionary Value list
# Using list comprehension + in operator
res = key in [sub for ele in test_dict['Gfg'] for sub in ele.keys()]

# printing result
print("Is key present in nested dictionary list ? : " + str(res))
