# Python3 program for the above approach

# Function to count for each array
# element, the number of elements
# that are smaller than that element
def smallerNumbers(arr, N):

	# Traverse the array
	for i in range(N):

		# Stores the count
		count = 0

		# Traverse the array
		for j in range(N):

			# Increment count
			if (arr[j] < arr[i]):
				count += 1

		# Print the count of smaller
		# elements for the current element
		print(count, end=" ")

# Driver Code
if __name__ == "__main__":

	arr = [3, 4, 1, 1, 2]
	N = len(arr)

	smallerNumbers(arr, N)

	# This code is contributed by ukasp.
