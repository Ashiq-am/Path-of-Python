# Function to return the cumulative sum list
def cumulative_list(old_list):
	new_list = [0] * len(old_list)

	# Adding the first element in the result list
	new_list[0] = old_list[0]

	# Adding the current element in the cumulative list
	for i in range(1, len(old_list)):
		new_list[i] = old_list[i] + new_list[i - 1]

	return new_list


# Driver code
if __name__ == "__main__":
	old_list = [10, 20, 30, 40, 50]

	print("Original List:")
	for item in old_list:
		print(item, end=" ")
	print()

	cumulative_list_result = cumulative_list(old_list)

	print("Cumulative Sum List:")
	for item in cumulative_list_result:
		print(item, end=" ")
