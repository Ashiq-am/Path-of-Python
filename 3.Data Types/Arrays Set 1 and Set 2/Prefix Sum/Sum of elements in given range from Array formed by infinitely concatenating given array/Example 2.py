# Python 3 program for the above approach

# Function to find the sum of elements
# in a given range of an infinite array
def rangeSum(arr, N, L, R):

	# Stores the prefix sum
	prefix = [0 for i in range(N + 1)]
	prefix[0] = 0

	# Calculate the prefix sum
	for i in range(1,N+1,1):
		prefix[i] = prefix[i - 1] + arr[i - 1]

	# Stores the sum of elements
	# from 1 to L-1
	leftsum = ((L - 1) // N) * prefix[N] + prefix[(L - 1) % N]

	# Stores the sum of elements
	# from 1 to R
	rightsum = (R // N) * prefix[N] + prefix[R % N]

	# Print the resultant sum
	print(rightsum - leftsum)

# Driver Code
if __name__ == '__main__':
	arr = [5, 2, 6, 9]
	L = 10
	R = 13
	N = len(arr)
	rangeSum(arr, N, L, R)

	# This code is contributed by SURENDRA_GANGWAR.
