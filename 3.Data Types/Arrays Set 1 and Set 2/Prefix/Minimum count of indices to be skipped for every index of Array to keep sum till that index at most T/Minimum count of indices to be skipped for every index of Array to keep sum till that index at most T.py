# Python3 approach for above approach

# Function to calculate minimum indices to be skipped
# so that sum till i remains smaller than T
def skipIndices(N, T, arr):
	# Store the sum of all indices before i
	sum = 0

	# Store the elements that can be skipped
	count = {}

	# Traverse the array, A[]
	for i in range(N):

		# Store the total sum of elements that
		# needs to be skipped
		d = sum + arr[i] - T

		# Store the number of elements need
		# to be removed
		k = 0

		if (d > 0):

			# Traverse from the back of map so
			# as to take bigger elements first
			for u in list(count.keys())[::-1]:
				j = u
				x = j * count[j]
				if (d <= x):
					k += (d + j - 1) // j
					break
				k += count[j]
				d -= x

		# Update sum
		sum += arr[i]

		# Update map with the current element
		count[arr[i]] = count.get(arr[i], 0) + 1

		print(k, end = " ")
# Driver code
if __name__ == '__main__':
	# Given Input
	N = 7
	T = 15
	arr = [1, 2, 3, 4, 5, 6, 7]

	# Function Call
	skipIndices(N, T, arr)

	# This code is contributed by mohit kumar 29.
