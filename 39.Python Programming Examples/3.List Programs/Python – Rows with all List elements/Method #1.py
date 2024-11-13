# Python3 code to demonstrate working of
# Rows with all List elements
# Using loop

# initializing list
test_list = [[7, 6, 3, 2], [5, 6], [2, 1, 8], [6, 1, 2]]

# printing original list
print("The original list is : " + str(test_list))

# initializing list
sub_list = [1, 2]

res = []
for row in test_list:

	flag = True

	# checking for all elements in list
	for ele in sub_list:
		if ele not in row:
			flag = False

	if flag:
		res.append(row)

# printing result
print("Rows with list elements : " + str(res))
