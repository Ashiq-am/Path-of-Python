# Python3 code to demonstrate working of
# Swap K suffix with prefix
# Using range swap + slice()

# initializing list
test_list = [5, 6, 3, 1, 0, 1, 3, 5, 7, 9]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 3

# performing range swap
test_list[:K], test_list[len(
	test_list) - K:] = test_list[len(test_list) - K:], test_list[:K]

# printing result
print("After prefix suffix swap : " + str(test_list))
