# Python3 code to demonstrate
# Multiplication till Null value
# using naive method

# initializing list of lists
test_list = [1, 3, 4, False, 4, 5, False, 7, 8]

# printing original list
print ("The original list is : " + str(test_list))

# Multiplication till Null value
# using naive method
for i in range(1, len(test_list)):
	if test_list[i]:
		test_list[i] *= test_list[i - 1]
	else:
		test_list[i] = 1

# printing result
print ("The computed modified new list : " + str(test_list))
