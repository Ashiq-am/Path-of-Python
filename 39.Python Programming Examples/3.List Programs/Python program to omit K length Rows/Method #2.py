# Python3 code to demonstrate working of
# Omit K length Rows
# Using filter() + lambda + len()

# initializing list
test_list = [[4, 7],
			[8, 10, 12, 8],
			[10, 11],
			[6, 8, 10]]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 4

# getting elements with length other than K
res = list(filter(lambda row : len(row) != K, test_list))

# printing result
print("Filtered Matrix : " + str(res))
