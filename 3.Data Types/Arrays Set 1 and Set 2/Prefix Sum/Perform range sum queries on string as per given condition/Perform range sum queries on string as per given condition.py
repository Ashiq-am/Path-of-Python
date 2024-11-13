# Python3 program for the above approach

# Function to perform range sum queries
# on string as per the given condition
def Range_sum_query(S, Query):

	# Initialize N by string size
	N = len(S)

	# Create array A[] for prefix sum
	A = [0] * N

	A[0] = ord(S[0]) - ord('a') + 1

	# Iterate till N
	for i in range(1, N):
		A[i] = ord(S[i]) - ord('a') + 1
		A[i] = A[i] + A[i - 1]

	# Traverse the queries
	for i in range(len(Query)):
		if(Query[i][0] == 1):

			# Check if if L == 1 range
			# sum will be A[R-1]
			print(A[Query[i][1] - 1])

		else:

			# Condition if L > 1 range sum
			# will be A[R-1] - A[L-2]
			print(A[Query[i][1] - 1] - A[Query[i][0] - 2])

# Driver Code

# Given string
S = "abcd"

Query = []

# Given Queries
Query.append([2, 4])
Query.append([1, 3])

# Function call
Range_sum_query(S, Query)
