# Python3 code to demonstrate working of
# Keys Values equal frequency
# Using loop

# initializing dictionary
test_dict = {5: 5, 8: 9, 7: 7, 1: 2, 10: 10, 4: 8}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

res = 0
for key in test_dict:

	# checking for equality and incrementing counter
	if key == test_dict[key]:
		res += 1

# printing result
print("The required frequency : " + str(res))
