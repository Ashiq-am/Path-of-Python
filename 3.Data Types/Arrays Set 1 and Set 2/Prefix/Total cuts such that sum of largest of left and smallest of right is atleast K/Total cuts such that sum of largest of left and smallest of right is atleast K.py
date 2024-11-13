# Function to find the total
# number of possible cuts


def totalCuts(N, K, A):
	max_val = -1
	index = 0
	count = 0
	minRight = [0] * N
	minRight[N - 1] = A[N - 1]

	# Loop to store the minimum from
	# right end till i
	for i in range(N - 2, -1, -1):
		if A[i] < minRight[i + 1]:
			minRight[i] = A[i]
		else:
			minRight[i] = minRight[i + 1]

	# Loop to find the number of
	# possible cuts
	for i in range(N - 1):
		max_val = max(max_val, A[i])
		if max_val + minRight[i + 1] >= K:
			count += 1

	return count


# Driver code
N = 3
K = 3
A = [1, 2, 3]

# Function call
result = totalCuts(N, K, A)
print(result)
