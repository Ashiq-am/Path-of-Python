# Python3 code to demonstrate working of
# Remove positional rows
# Using enumerate() + list comprehension

# initializing list
test_list = [[3, 5, 2], [1, 8, 9], [5, 3, 1],
			[0, 1, 6], [9, 4, 1], [1, 2, 10],
			[0, 1, 2]]

# printing original list
print("The original list is: " + str(test_list))

# initializing indices
idx_lis = [1, 2, 5]

# using enumerate() to get index and value of each row
res = [sub[1] for sub in enumerate(test_list) if sub[0] not in idx_lis]

# printing result
print("Matrix after removal: " + str(res))
