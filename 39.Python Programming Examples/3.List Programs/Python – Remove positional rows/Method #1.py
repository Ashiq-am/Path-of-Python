# Python3 code to demonstrate working of
# Remove positional rows
# Using loop + pop() + back iteration

# initializing list
test_list = [[3, 5, 2], [1, 8, 9], [5, 3, 1],
			[0, 1, 6], [9, 4, 1], [1, 2, 10],
			[0, 1, 2]]

# printing original list
print("The original list is: " + str(test_list))

# initializing indices
idx_lis = [1, 2, 5]

# back iteration
for idx in idx_lis[::-1]:

	# pop() used for removal
	test_list.pop(idx)

# printing result
print("Matrix after removal: " + str(test_list))
