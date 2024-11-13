def queries_to_find_LR(s, n, q, m):
	"""
	Function to answer Queries to find the number of characters
	repeated twice in a row in the substring L to R
	"""
	# Declaring Prefix Sum array
	prefix_sum = [0] * (n + 1)

	# Populating Prefix array
	for i in range(1, n):
		# if the last two characters are the same
		if s[i] == s[i - 1]:
			prefix_sum[i + 1] += 1

	# taking the prefix sum of this array
	for i in range(1, n + 1):
		prefix_sum[i] = prefix_sum[i] + prefix_sum[i - 1]

	# iterate for M queries
	for i in range(m):
		# query to find the answer in L to R
		L, R = q[i][0], q[i][1]

		# number of indexes which have repeated characters in a row
		number_of_indexes = prefix_sum[R] - prefix_sum[L - 1]

		# if L - 1 was equal to L, subtract 1
		if L - 2 >= 0 and s[L - 1] == s[L - 2]:
			number_of_indexes -= 1

		# answer for the query
		print(number_of_indexes, end=" ")

	# finish on the next line for the next test case
	print()


# Driver Code
if __name__ == "__main__":
	# Input 1
	N, M = 11, 4
	S = "mississippi"
	Q = [[3, 9], [8, 10], [4, 6], [7, 7]]

	# Function Call
	queries_to_find_LR(S, N, Q, M)
