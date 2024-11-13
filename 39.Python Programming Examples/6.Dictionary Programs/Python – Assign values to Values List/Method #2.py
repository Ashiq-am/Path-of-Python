# Python3 code to demonstrate working of
# Assign values to Values List
# Using items() + dictionary comprehension

# initializing dictionary
test_dict = {'Gfg': [3, 6],
			'is': [4, 2],
			'best': [9]}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# initializing lookup dict
look_dict = {3: [1, 5], 6: "Best", 4: 10, 9: 12, 2: "CS"}

# nested dictionaries to sought solution
# items() used to access key-val pairs
res = {key: {ikey: ival for (ikey, ival) in look_dict.items(
) if ikey in val} for (key, val) in test_dict.items()}

# printing result
print("The mapped dictionary : " + str(res))
