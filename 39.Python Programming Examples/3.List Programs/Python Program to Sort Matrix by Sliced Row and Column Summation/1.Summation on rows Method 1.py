# get sliced summation
def get_sliced_sum(row):
	return sum(row[i:j])


# initializing list
test_list = [[1, 4, 3, 1, 3], [3, 4, 5, 2, 4],
			[23, 5, 5, 3], [2, 3, 5, 1, 6]]

# printing original list
print("The original list is : " + str(test_list))

# initializing range
i, j = 1, 3

# performing sort
test_list.sort(key=get_sliced_sum)

# printing result
print("Sorted List : " + str(test_list))
