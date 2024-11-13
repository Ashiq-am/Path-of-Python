# get sliced summation
def get_sliced_sum(row):
	return sum(row[i:j])


# initializing list
test_list = [[1, 4, 3, 1], [3, 4, 5, 2],
			[23, 5, 5, 3], [2, 3, 5, 1]]

# printing original list
print("The original list is : " + str(test_list))

# initializing range
i, j = 1, 3

# transposing matrix
test_list = list(zip(*test_list))

# performing sort
test_list.sort(key=get_sliced_sum)

# performing transpose again to get
# result.
test_list = zip(*test_list)

# converting list of tuples to list of
# lists
res = [list(sub) for sub in test_list]

# printing result
print("Sorted List Columnwise : " + str(res))
