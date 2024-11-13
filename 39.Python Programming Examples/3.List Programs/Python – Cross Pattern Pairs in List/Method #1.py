# Python3 code to demonstrate working of
# Cross Pattern Pairs in List
# Using loop


# function to generate cross pattern pairs
def crossPair(test_list1, test_list2):

	# lengths of both lists should be equal
	if len(test_list1) != len(test_list2):
		return -1

	res = []
	for idx in range(len(test_list1)):

		# checking for conditions
		if idx % 2 == 0:
			res.append((test_list1[idx], test_list2[idx + 1]))
		else:
			res.append((test_list1[idx], test_list2[idx - 1]))
	return res


# initializing lists
input_list1 = [4, 5, 6, 2, 8, 9]
input_list2 = [9, 1, 4, 7, 9, 2]

# printing original lists
print("The original list 1 is : " + str(input_list1))
print("The original list 2 is : " + str(input_list2))

# printing result
print("Paired List elements : ", crossPair(input_list1, input_list2))
