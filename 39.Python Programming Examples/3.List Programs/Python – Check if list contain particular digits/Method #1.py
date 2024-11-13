# Python3 code to demonstrate working of
# Test if list contain particular digits
# Using loop + str() + join()

# initializing lists
test_list = [435, 133, 113, 451, 134]

# printing original list
print("The original list is : " + str(test_list))

# initializing digits
digs = [1, 4, 5, 3]

digt_str = ''.join([str(ele) for ele in digs])
all_ele = ''.join([str(ele) for ele in test_list])

res = True
for ele in all_ele:

	# checking for all digits in element string
	for el in ele:
		if el not in digt_str:
			res = False
			break

# printing result
print("Are all elements made from required digits? : " + str(res))
