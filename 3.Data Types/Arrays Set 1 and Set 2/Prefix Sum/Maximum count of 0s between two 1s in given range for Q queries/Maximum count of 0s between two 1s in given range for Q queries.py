# Function to count the number of
# 0s lying between the two 1s for
# each query
def countOsBetween1s(S, N, Q):

	# Stores count of 0's that are
	# right to the most recent 1's
	leftBound = [0]*N

	# Stores count of 0's that are
	# left to the most recent 1's
	rightBound = [0]*N

	# Stores the count of zeros
	# in a prefix/suffix of array
	count = 0

	# Stores the count of total 0s
	total = 0

	# Traverse the string S
	for i in range(N):

		# If current character is
		# '1'
		if (S[i] == '1'):
			count = total

		# Otherwise
		elif (S[i] == '0'):
			total += 1

		# Update the rightBound[i]
		rightBound[i] = count

	# Update count and total to 0
	count = 0
	total = 0

	# Traverse the string S in
	# reverse manner
	for i in range(N - 1, -1, -1):

		# If current character is
		# '1'
		if (S[i] == '1'):
			count = total

		# Otherwise
		elif (S[i] == '0'):
			total += 1

		# Update the leftBound[i]
		leftBound[i] = count

	# Traverse given query array
	for q in range(2):

		L = Q[q][0]
		R = Q[q][1]

		# Update the value of count
		count = leftBound[L] + rightBound[R] - total

		# Print the count as the
		# result to the current
		# query [L, R]
		print(count, end=" ")


# Driver Code
if __name__ == "__main__":

	S = "1001010"
	Q = [[0, 4], [0, 5]]
	N = len(S)
	countOsBetween1s(S, N, Q)

	# This code is contributed by ukasp.
