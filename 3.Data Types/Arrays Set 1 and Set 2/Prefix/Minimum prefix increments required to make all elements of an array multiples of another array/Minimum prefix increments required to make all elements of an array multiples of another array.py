# Python3 program for the above approach
from math import ceil,floor

# Function to find minimum count of operations
# required to make A[i] multiple of B[i] by
# incrementing prefix subarray
def MinimumMoves(A, B, N):

	# Stores minimum count of operations
	# required to make A[i] multiple of B[i]
	# by incrementing prefix subarray
	totalOperations = 0

	# Stores the carry
	carry = 0

	# Stores minimum difference of
	# correspoinding element in
	# prefix subarray
	K = 0

	# Traverse the array
	for i in range(N - 1, -1, -1):

		# Stores the closest greater or equal number
		# to A[i] which is a multiple of B[i]
		nearestMultiple = ceil((A[i] + carry)/ B[i])* B[i]

		# Stores minimum difference
		K = nearestMultiple - (A[i] + carry)

		# Update totalOperations
		totalOperations += K

		# Update carry
		carry += K
	return totalOperations

# Driver Code
if __name__ == '__main__':

	# Input arrays A[] and B[]
	A = [3, 4, 5, 2, 5, 5, 9]
	B = [1, 1, 9, 6, 3, 8, 7]

	# Length of arrays
	N = len(A)
	print (MinimumMoves(A, B, N))

# This code is contributed by mohit kumar 29.
