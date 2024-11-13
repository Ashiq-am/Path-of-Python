# Function to Minimize sum of array by replacing
# initial L elements with X and R elements from
# end with Y


def minimumSum(N, A, X, Y):
	# Declaring 2 arrays Pre[] and Suff[] to
	# store the minimum possible sum of each
	# subarray from beginning and end respectively
	Pre = [0] * (N + 1)
	Suff = [0] * (N + 1)
	Pre[0], Suff[0] = 0, 0

	# Initializing answer as a large value
	answer = float('inf')

	# Iterating through 1 to N and Calculating
	# the values of Pre and Suff for each index
	for i in range(1, N + 1):
		Pre[i] = min(X * i, Pre[i - 1] + A[i - 1])
		Suff[i] = min(Y * i, Suff[i - 1] + A[N - i])

	# Calculating answer as the minimum of
	# all possible Pre[i]+Suff[N-i]
	for i in range(N + 1):
		answer = min(answer, Pre[i] + Suff[N - i])

	# Returning final answer
	return answer


# Driver code
N = 5
X = 4
Y = 3
A = [5, 5, 0, 6, 3]

# Function call
ans = minimumSum(N, A, X, Y)
print(ans)
