# Python3 program for the above approach

# Function to find the maximum sum of
# MEX of prefix arrays for any
# arrangement of the given array
def maximumMex(arr, N):

	# Stores the final arrangement
	ans = []

	# Sort the array in increasing order
	arr = sorted(arr)

	# Iterate over the array arr[]
	for i in range(N):
		if (i == 0 or arr[i] != arr[i - 1]):
			ans.append(arr[i])

	# Iterate over the array, arr[]
	# and push the remaining occurrences
	# of the elements into ans[]
	for i in range(N):
		if (i > 0 and arr[i] == arr[i - 1]):
			ans.append(arr[i])

	# Print the array, ans[]
	for i in range(N):
		print(ans[i], end = " ")

# Driver Code
if __name__ == '__main__':

	# Given array
	arr = [1, 0, 0 ]

	# Store the size of the array
	N = len(arr)

	# Function Call
	maximumMex(arr, N)

# This code is contributed by mohit kumar 29.
