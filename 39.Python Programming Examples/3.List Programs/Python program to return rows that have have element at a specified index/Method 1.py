# initializing lists
test_list1 = [[1, 8, 3], [9, 2, 0], [6, 4, 4], [6, 4, 4]]
test_list2 = [[1, 9, 3], [8, 2, 3], [5, 4, 6], [5, 4, 6]]

# printing original lists
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

# initializing K
K = 1

res = []
for idx in range(len(test_list1)):

	# comparing lists
	if test_list1[idx][K] == test_list2[idx][K]:
		res.append(test_list1[idx])
		res.append(test_list2[idx])


# printing result
print("K index matching rows : " + str(res))
