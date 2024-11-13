# Python code for the above approach

# Function to determine if there is only
# one subarray containing K 1s, after
# replacing each 2 with either 0 or 1
def isPossible(A, N, K):

	# s0 stores the number of zeroes till
	# each index s1 stores the number of
	# ones till each index
	s0 = [0] * (N + 1)
	s1 = [0] * (N + 1)
	s0[0] = s1[0] = 0

	# Filling the values of s0 and s1
	# for each index
	for i in range(N):
		s0[i + 1] = s0[i] + (1 if A[i] == 0 else 0)
		s1[i + 1] = s1[i] + (1 if A[i] == 1 else 0)

	answer = 0

	# Traversing from i = 0 to N - K and
	# checking if both the conditions are
	# satisfied for any index
	i = 0
	while(i + K <= N):
		c0 = s0[i + K] - s0[i]
		c1 = s1[i + K] - s1[i]

		# Checking the condition that all
		# the 1s are present in the current
		# subarray and there are no zeroes
		if (c0 == 0 and c1 == s1[N]):
			answer += 1
		i = i + 1


	# Return the correct ansewr based on the
	# count of indices
	if (answer == 1):
		return "YES"
	elif (answer == 0):
		return "NO"
	else:
		return "MULTIPLE"


# Driver code
N = 3
K = 2
A = [1, 2, 2]

# Function Call
print(isPossible(A, N, K))


