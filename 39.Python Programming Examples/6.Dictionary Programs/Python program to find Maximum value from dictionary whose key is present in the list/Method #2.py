# Python3 code to demonstrate working of
# Maximum value from List keys
# Using max() + list comprehension

# initializing dictionary
test_dict = {"Gfg": 4, "is" : 5, "best" : 9,
			"for" : 11, "geeks" : 3}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# initializing list
test_list = ["Gfg", "best", "geeks"]

# maximum is 11, but not present in list,
# hence 9 is output.
res = max([test_dict[ele] for ele in test_list
		if ele in test_dict])

# printing result
print("The required maximum : " + str(res))
