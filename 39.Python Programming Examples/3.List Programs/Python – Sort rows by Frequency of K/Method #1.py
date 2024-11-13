# Python3 code to demonstrate working of
# Sort rows by Frequency of K
# Using sort() + count()


def get_Kfreq(row):

	# return Frequency
	return row.count(K)


# initializing list
test_list = [[10, 2, 3, 2, 3], [5, 5, 4, 7, 7, 4], [1, 2], [1, 1, 2, 2, 2]]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
K = 2

# performing inplace sort
test_list.sort(key=get_Kfreq)

# printing result
print("Sorted List : " + str(test_list))
