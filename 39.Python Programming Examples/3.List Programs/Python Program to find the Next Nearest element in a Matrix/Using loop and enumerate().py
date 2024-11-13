# get Nearest coord.
def near_coord(test_list, x, y, val):
	for idx, row in enumerate(test_list[x:]):
		for j, ele in enumerate(row):

			# checking for value at lower formed rectangle
			if ele == val and j > y:
				return idx + x, j

	# if no index found
	return -1, -1


# initializing list
test_list = [[4, 3, 1, 2, 3], [7, 5, 3, 6, 3],
			[8, 5, 3, 5, 3], [1, 2, 3, 4, 6]]

# printing original list
print("The original list is : " + str(test_list))

# initializing check coord
i, j = 1, 3

# initializing K
K = 3

# getting nearest coordinates
res_abs, res_ord = near_coord(test_list, i, j, K)

# printing result
print("Found K index : " + str((res_abs, res_ord)))
