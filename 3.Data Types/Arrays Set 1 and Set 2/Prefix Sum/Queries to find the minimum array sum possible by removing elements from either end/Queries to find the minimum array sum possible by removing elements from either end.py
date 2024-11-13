# Python3 program for the above approach

# Function to find the minimum sum for
# each query after removing elements
# from either ends
def minSum(arr, N, Q, M):

	# Traverse the query array
	for i in range(M):
		val = Q[i]

		front, rear = 0, 0

		# Traverse the array from
		# the front
		for j in range(N):
			front += arr[j]

			# If element equals val,
			# then break out of loop
			if (arr[j] == val):
				break

		# Traverse the array from rear
		for j in range(N - 1, -1, -1):
			rear += arr[j]

			# If element equals val, break
			if (arr[j] == val):
				break

		# Prthe minimum of the
		# two as the answer
		print(min(front, rear), end = " ")

# Driver Code
if __name__ == '__main__':
	arr = [2, 3, 6, 7, 4, 5, 1]
	N = len(arr)
	Q = [7, 6]
	M = len(Q)

	# Function Call
	minSum(arr, N, Q, M)
