# code by flutterfly
def Max_sum(N, A):
	# Prefix and Suffix Arrays
	prefix = [0] * N
	suffix = [0] * N

	# Initializing prefix array
	prefix[0] = A[0]
	for i in range(1, N):
		prefix[i] = max(prefix[i - 1], A[i])

	# Initializing suffix array
	suffix[N - 1] = A[N - 1]
	for i in range(N - 2, -1, -1):
		suffix[i] = max(suffix[i + 1], A[i])

	# Variable to store max sum
	sum_val = 0

	# Calculating sum for all middle elements
	for i in range(1, N - 1):
		maxi1, maxi2 = prefix[i], suffix[i]
		sum_val += min(maxi1, maxi2)

	# Adding last elements of both ends into sum
	sum_val += A[0] + A[N - 1]

	# Printing the value of sum
	print(sum_val)

# Input
N = 2
A = [5, 2]

# Function call
Max_sum(N, A)
