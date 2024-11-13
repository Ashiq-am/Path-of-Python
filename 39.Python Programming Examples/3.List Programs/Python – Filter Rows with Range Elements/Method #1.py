# Python3 code to demonstrate working of
# Filter Rows with Range Elements
# Using all() + list comprehension

# initializing list
test_list = [[3, 2, 4, 5, 10], [3, 2, 5, 19],
			[2, 5, 10], [2, 3, 4, 5, 6, 7]]

# printing original list
print("The original list is : " + str(test_list))

# initializing range
i, j = 2, 5

# checking for presence of all elements using in operator
res = [sub for sub in test_list if all(ele in sub for ele in range(i, j + 1))]

# printing result
print("Extracted rows : " + str(res))
