# Python3 code to demonstrate working of
# Element-wise Matrix Difference
# Using loop + zip()

# initializing lists
test_list1 = [[2, 4, 5], [5, 4, 2], [1, 2, 3]]
test_list2 = [[6, 4, 6], [9, 6, 3], [7, 5, 4]]

# printing original lists
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

res = []

# iterating for rows
for sub1, sub2 in zip(test_list1, test_list2):
	temp = []

	# interate for elements
	for ele1, ele2 in zip(sub1, sub2):
		temp.append(ele2 - ele1)
	res.append(temp)

# printing result
print("The Matrix Difference : " + str(res))
