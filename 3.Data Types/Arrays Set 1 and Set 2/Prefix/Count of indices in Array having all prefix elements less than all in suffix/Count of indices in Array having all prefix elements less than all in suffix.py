# Python3 implementation of the approach
INT_MIN = -2147483648
INT_MAX = 2147483647

# Function to return total count
# of sorted points in the array
def countSortedPoints(arr, N):

	left = [0 for i in range(N)]
	right = [0 for i in range(N)]

	# Initialize the variables
	Min = INT_MAX
	Max = INT_MIN
	Count = 0

	# Make Maximum array
	for i in range(N):

		Max = max(arr[i], Max)
		left[i] = Max

			# Make Minimum array
	for i in range(N - 1, -1, -1):

		Min = min(arr[i], Min)
		right[i] = Min

	# Count of sorted points
	for i in range(0, N - 1):
		if (left[i] <= right[i + 1]):
			Count += 1

			# Return count of sorted points
	return Count

# Driver Code
arr = [1, 5, 4, 2, 3, 8, 7, 9]
N = len(arr)

# Function call
print(countSortedPoints(arr, N))

# This code is contributed by shinjanpatra
