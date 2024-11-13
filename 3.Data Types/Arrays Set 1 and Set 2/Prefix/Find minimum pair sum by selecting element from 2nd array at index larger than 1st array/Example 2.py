# Python 3 program for above approach
import sys

# Function to calculate minimum sum
def minimumCost(A, B, N):

	# For storing the minimum value
	# from rear end of B[]
	cheapestPossible = [0]*N

	# Only one possible value on last index
	cheapestPossible[N - 1] = B[N - 1]

	for i in range(N - 2 ,- 1, -1):

		# The lowest possible sum at
		# index i and above
		cheapestPossible[i] = min(cheapestPossible[i + 1],
								B[i])

	# For storing minimum sum
	minimumPrice = sys.maxsize

	# Adding the current value of A[] and
	# minimum value of B[] after i and
	# comparing it with the last minimum sum
	for i in range(N):
		minimumPrice = min(minimumPrice,
						A[i] + cheapestPossible[i])

	return minimumPrice

# Driver Code
if __name__ == "__main__":

	A = [34, 12, 45, 10, 86, 39, 77]
	B = [5, 42, 29, 63, 30, 33, 20]
	N = len(A)

	# Function Call
	print(minimumCost(A, B, N))

	# This code is contributed by ukasp.
