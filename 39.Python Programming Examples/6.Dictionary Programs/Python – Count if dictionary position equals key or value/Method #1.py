# Python3 code to demonstrate working of
# Count if dictionary position equals key or value
# Using loop

# initializing dictionary
test_dict = {5: 3, 1: 3, 10: 4, 7: 3, 8: 1, 9: 5}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

res = 0
test_dict = list(test_dict.items())
for idx in range(0, len(test_dict)):

	# checking for key or value equality
	if idx == test_dict[idx][0] or idx == test_dict[idx][1]:
		res += 1

# printing result
print("The required frequency : " + str(res))
