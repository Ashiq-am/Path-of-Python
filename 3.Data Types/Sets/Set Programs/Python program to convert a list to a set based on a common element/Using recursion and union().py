# utility function
def common_set(test_set):
	for idx, val in enumerate(test_set):
		for j, k in enumerate(test_set[idx + 1:], idx + 1):

			# getting union by conditions
			if val & k:
				test_set[idx] = val.union(test_set.pop(j))
				return common_set(test_set)
	return test_set

# utility function


# initializing lists
test_list = [[15, 14, 12, 18], [9, 5, 2, 1], [4, 3, 2, 1], [19, 11, 13, 12]]

# printing original list
print("The original list is : " + str(test_list))

test_set = list(map(set, test_list))

# calling recursive function
res = common_set(test_set)

# printing result
print("Common element groups : " + str(res))
