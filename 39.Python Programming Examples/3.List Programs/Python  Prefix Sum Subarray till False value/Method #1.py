# Python3 code to demonstrate
# Prefix Sum Subarray till False value
# using naive method

# initializing list of lists
test_list = [1, 3, 4, 0, 4, 5, 0, 7, 8]

# printing original list
print ("The original list is : " + str(test_list))

# Prefix Sum Subarray till False value
# using naive method
for i in range(1, len(test_list)):
	if test_list[i]:
		test_list[i] += test_list[i - 1]

# printing result
print ("The computed modified new list : " + str(test_list))
