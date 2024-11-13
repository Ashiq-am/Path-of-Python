# Python3 code to demonstrate working of
# Concatenate 2 Matrix Row-wise
# Using loop + enumerate()

# initializing lists
test_list1 = [[4, 3, 5, ], [1, 2, 3], [3, 7, 4]]
test_list2 = [[1, 3], [9, 3, 5, 7], [8]]

# printing original lists
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

for idx, ele in enumerate(test_list1):
	new_vals = []

	# getting all values at same index row
	for ele in test_list2[idx]:
		new_vals.append(ele)

	# extending the initial matrix
	test_list1[idx].extend(new_vals)

# printing result
print("The concatenated Matrix : " + str(test_list1))
