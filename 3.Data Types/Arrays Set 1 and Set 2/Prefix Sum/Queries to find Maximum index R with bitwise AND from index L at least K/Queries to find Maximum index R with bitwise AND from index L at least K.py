# Function to check if bitwise AND from L to R
# is at least K or not


def ispos(L, R, K, pre):
	# size of range
	sze = R - L + 1

	# to store bitwise AND from L to R
	bitwiseANDLtoR = 0

	# iterate for ith bit
	for i in range(1, 32):

		# number of bits from Range L to R for ith position
		numBit = pre[R][i] - pre[L - 1][i]

		# if the number of bits in the range L to R
		# is equal to the size of the range
		if sze == numBit:
			# i'th bit will contribute 2 ^ (i - 1)
			bitwiseANDLtoR += (1 << (i - 1))

	# return true if bitwise AND from L
	# to R is at least K
	return bitwiseANDLtoR >= K


# Function for Queries to find Maximum index R
# with bitwise AND from index L at least K
def minimizeMaximumAbsDiff(A, N, Q, M):
	# initialize prefix array
	pre = [[0] * 33 for _ in range(N + 1)]

	# Fill prefix array with bits of N elements
	for i in range(N):
		# iterate over all bits
		for j in range(32):
			# if j'th bit is set increment prefix array
			if (1 << j) & A[i]:
				pre[i + 1][j + 1] += 1

	# Take prefix sum
	for i in range(1, N + 1):
		for j in range(1, 32):
			pre[i][j] += pre[i - 1][j]

	for i in range(M):
		# Range of binary search
		low, high = Q[i][0], N

		# Running loop until high
		# is not equal to low
		while high - low > 1:
			# mid is average of low and high
			mid = (low + high) // 2

			# Checking test function
			if ispos(Q[i][0], mid, Q[i][1], pre):
				low = mid
			else:
				high = mid - 1

		# Checking whether high can be the answer
		if ispos(Q[i][0], high, Q[i][1], pre):
			print(high, end=' ')

		# Checking whether low can be the answer
		elif ispos(Q[i][0], low, Q[i][1], pre):
			print(low, end=' ')
		else:
			print(-1, end=' ')

	print()


# Driver Code
# Input 1
N = 5
A = [15, 14, 17, 42, 34]
M = 3
Q = [[1, 7], [2, 15], [4, 5]]

# Function Call
minimizeMaximumAbsDiff(A, N, Q, M)

# Input 2
N1 = 5
A1 = [7, 5, 3, 1, 7]
M1 = 2
Q1 = [[1, 7], [2, 3]]

# Function Call
minimizeMaximumAbsDiff(A1, N1, Q1, M1)
