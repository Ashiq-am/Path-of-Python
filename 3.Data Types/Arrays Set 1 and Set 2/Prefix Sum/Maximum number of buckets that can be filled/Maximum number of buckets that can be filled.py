# Python3 program for the above approach

# Function to find the maximum number
# of buckets that can be filled with
# the amount of water available
def getBuckets(arr, N) :

	# Find the total available water
	availableWater = N * (N - 1) // 2

	# Sort the array in ascending order
	arr.sort()

	i, Sum = 0, 0

	# Check if bucket can be
	# filled with available water
	while (Sum <= availableWater) :
		Sum += arr[i]
		i += 1

	# Print count of buckets
	print(i - 1, end = "")

arr = [ 1, 5, 3, 4, 7, 9 ]
N = len(arr)

getBuckets(arr, N);

# This code is contributed by divyeshrabadiya07.
