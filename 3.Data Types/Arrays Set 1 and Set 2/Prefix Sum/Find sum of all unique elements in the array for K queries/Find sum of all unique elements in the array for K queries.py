# Python implementation to find the
# sum of all unique elements of
# the array after Q queries

# Function to find the sum of
# unique elements after Q Query
def uniqueSum(A, R, N, M) :

	# Updating the array after
	# processing each query
	for i in range(0, M) :

		l = R[i][0]
		r = R[i][1] + 1

		# Making it to 0-indexing
		l -= 1
		r -= 1
		A[l] += 1

		if (r < N) :
			A[r] -= 1

	# Iterating over the array
	# to get the final array
	for i in range(1, N) :
		A[i] += A[i - 1]

	# Variable to store the sum
	ans = 0

	# Hash to maintain perviously
	# occured elements
	s = {chr}

	# Loop to find the maximum sum
	for i in range(0, N) :
		if (A[i] not in s) :
			ans += A[i]

		s.add(A[i])

	return ans

# Driver code
A = [ 0, 0, 0, 0, 0, 0 ]
R = [ [ 1, 3 ], [ 4, 6 ],
	[ 3, 4 ], [ 3, 3 ] ]
N = len(A)
M = len(R)

print(uniqueSum(A, R, N, M))
