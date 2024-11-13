# Python3 code to demonstrate
# Extracting specifix keys from dictionary
# Using dict()

# initializing dictionary
test_dict = {'nikhil' : 1, "akash" : 2, 'akshat' : 3, 'manjeet' : 4}

# printing original list
print("The original dictionary : " + str(test_dict))

# Using dict()
# Extracting specifix keys from dictionary
res = dict((k, test_dict[k]) for k in ['nikhil', 'akshat']
										if k in test_dict)

# print result
print("The filtered dictionary is : " + str(res))
