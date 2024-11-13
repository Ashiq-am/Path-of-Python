# Python3 code to demonstrate working of
# Dictionary Keys Summation
# Using loop

# initializing dictionary
test_dict = {3: 4, 9: 10, 15: 10, 5: 7, 6: 7}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

res = 0
for key in test_dict:

	# adding keys
	res += key

# printing result
print("The dictionary keys summation : " + str(res))
