# Python3 code to demonstrate working of
# Nearest occurrence of x from y in List
# Using list comprehension + loop + index()


# function to find index of nearest
# occurance between two elements
def nearestOccuranceIndex(test_list, x, y):

	# checking if both elements are present in list
	if x not in test_list or y not in test_list:
		return -1
	# getting indices of x
	x_idx = [idx for idx in range(len(test_list)) if test_list[idx] == x]

	# getting y index
	y_idx = test_list.index(y)

	# getting min_dist index
	min_dist = 1000000
	res = None
	for ele in x_idx:

		# checking for min ele, and updating index
		if abs(ele - y_idx) < min_dist:
			res = ele
			min_dist = abs(ele - y_idx)
	return res


# initializing list
input_list = [2, 4, 5, 7, 8, 6, 3, 8, 4, 2, 0, 9, 4, 9, 4]

# printing original list
print("The original list is : " + str(input_list))

# initializing x
x = 4

# initializing y
y = 6

# printing result
print("Minimum distance index: ", nearestOccuranceIndex(input_list, x, y))
