# Python Implementation

def special_xor(N, Q, a, queries):
	# Calculate prefix XOR array
	x = [0] * N
	x[0] = a[0]
	for i in range(1, N):
		x[i] = a[i] ^ x[i - 1]

	ans = []

	sep_xor = 0
	for i in range(Q):
		l, r = queries[i][0] - 1, queries[i][1] - 1

		# Calculate XOR of [L, R] using prefix XOR values
		if l == 0:
			sep_xor = x[r]
		else:
			sep_xor = x[r] ^ x[l - 1]

		# XOR with the XOR of the entire array to get the
		# final result
		ans.append(x[N - 1] ^ sep_xor)

	return ans

# Input parameters
N, Q = 10, 3
a = [4, 7, 8, 5, 9, 6, 1, 0, 20, 10]
queries = [(3, 8), (1, 6), (2, 3)]

# Call the special_xor function
result = special_xor(N, Q, a, queries)

# Print the results
print("Results:", *result)


# This code is contributed by Tapesh(tapeshdua420)
