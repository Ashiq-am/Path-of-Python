# Python code for the above approach
def score_of_sorted_array(A, B, N, M):
	# Initializing suffix sum and prefix sum arrays
	sufSum = [0] * N
	preSum = [0] * N

	# Computing suffix sum array
	sufSum[N - 1] = A[N - 1]
	for i in range(N - 2, -1, -1):
		sufSum[i] = sufSum[i + 1] + A[i]

	# Computing prefix sum array
	preSum[0] = A[0]
	for i in range(1, N):
		preSum[i] = preSum[i - 1] + A[i]

	res = 0
	for i in range(M):
		# Adding suffix sum of last B[i] elements
		res += sufSum[B[i]]
		# Subtracting prefix sum of first N-B[i]-1 elements
		res -= preSum[N - B[i] - 1]

	return res


# Driver code
N = 4
M = 2
A = [1, 2, 3, 4]
B = [1, 3]

# Function call
print(score_of_sorted_array(A, B, N, M))
