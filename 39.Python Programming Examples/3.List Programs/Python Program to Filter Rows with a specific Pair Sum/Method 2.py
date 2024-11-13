# get pair sum
def pair_sum(x, k):

	# checking pair sum
	for idx in range(len(x)):
		for ix in range(idx + 1, len(x)):
			if x[idx] + x[ix] == k:
				return True
	return False


# initializing list
test_list = [[1, 5, 3, 6], [4, 3, 2, 1], [7, 2, 4, 5], [6, 9, 3, 2]]

# printing original list
print("The original list is : " + str(test_list))

# initializing K
k = 8

# checking for pair sum
# filtering using filter() and lambda
res = list(filter(lambda ele: pair_sum(ele, k), test_list))

# printing result
print("Filtered Rows : " + str(res))
