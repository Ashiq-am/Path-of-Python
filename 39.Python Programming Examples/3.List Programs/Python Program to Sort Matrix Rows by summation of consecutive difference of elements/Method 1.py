# get abs summation
def diff_sum(row):
	return sum([abs(row[idx + 1] - row[idx]) for idx in range(0, len(row) - 1)])


# initializing list
test_list = [[1, 5, 3, 6], [4, 3, 2, 1], [7, 2, 4, 5], [6, 9, 3, 2]]

# printing original list
print("The original list is : " + str(test_list))

# performing inplace sort
test_list.sort(key=diff_sum)

# printing result
print("Sorted Rows : " + str(test_list))
