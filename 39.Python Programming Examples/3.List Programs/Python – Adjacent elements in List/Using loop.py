# Python3 code to demonstrate working of
# Adjacent elements in List
# Using loop


# Function to find adjacent
# elements in List
def findAdjacentElements(test_list):
	res = []
	for idx, ele in enumerate(test_list):

		# Checking for all cases to append
		if idx == 0:
			res.append((None, test_list[idx + 1]))
		elif idx == len(test_list) - 1:
			res.append((test_list[idx - 1], None))
		else:
			res.append((test_list[idx - 1], test_list[idx + 1]))
	return res


# Initializing list
input_list = [3, 7, 8, 2, 1, 5, 8, 9, 3]

# Printing original list
print("The original list is:", input_list)


# printing result
print("The Adjacent elements list:", findAdjacentElements(input_list))
