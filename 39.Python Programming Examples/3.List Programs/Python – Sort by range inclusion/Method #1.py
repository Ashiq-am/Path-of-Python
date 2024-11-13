# Python3 code to demonstrate working of
# Sort by range inclusion
# Using sort() + sum()


def range_sum(row):

	# summing in range element
	return sum([abs(sub[1] - sub[0]) for sub in row if sub[0] > i and sub[0] < j and sub[1] > i and sub[1] < j])


# initializing list
test_list = [[(1, 5), (6, 10), (10, 15)], [(3, 16)], [
	(2, 4), (6, 8), (9, 14)], [(1, 3), (9, 13)]]

# printing original list
print("The original list is : " + str(test_list))

# initializing range
i, j = 2, 15

# inplace sorting using sort()
test_list.sort(key=range_sum)

# printing result
print("Sorted List : " + str(test_list))
