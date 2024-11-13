# Python3 code to demonstrate
# Indices of sorted list of list elements
# using sorted() + lambda

# initializing list
test_list = [[4, 5, 1],
			[9, 3, 2],
			[8, 6]]

# printing original list
print("The original list : " + str(test_list))

# using sorted() + lambda
# Indices of sorted list of list elements
res = sorted([(i, j) for i, x in enumerate(test_list)
							for j, k in enumerate(x)],
			key = lambda ij: test_list[ij[0]][ij[1]])

# print result
print("The indices of sorted order are : " + str(res))
