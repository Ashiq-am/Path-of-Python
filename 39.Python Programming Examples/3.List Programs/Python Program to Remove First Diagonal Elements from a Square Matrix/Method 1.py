# initializing list
test_list = [[5, 3, 3, 2, 1], [5, 6, 7, 8, 2], [
	9, 3, 4, 6, 7], [0, 1, 2, 3, 5], [2, 5, 4, 3, 5]]

# printing original list
print("The original list is : " + str(test_list))

res = []
for idx, ele in enumerate(test_list):

	# removing element whose index is equal to row index
	res.append([el for idxx, el in enumerate(ele) if idxx != idx])

# printing result
print("Filtered Matrix : " + str(res))
