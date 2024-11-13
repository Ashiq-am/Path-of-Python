# Python3 code to demonstrate working of
# Filter Rows with Range Elements
# Using filter() + lambda + all()

# initializing list
test_list = [[3, 2, 4, 5, 10], [3, 2, 5, 19],
			[2, 5, 10], [2, 3, 4, 5, 6, 7]]

# printing original list
print("The original list is : " + str(test_list))

# initializing range
i, j = 2, 5

# filter() and lambda used to filter elements
res = list(filter(lambda sub: all(
	ele in sub for ele in range(i, j + 1)), test_list))

# printing result
print("Extracted rows : " + str(res))
