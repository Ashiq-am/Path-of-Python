# Python code for the above approach
from queue import PriorityQueue

# Function to find the largest subsequence
# satisfying given conditions
def FindMaxSubsequence(a, n):

	# Min priority queue
	v = PriorityQueue()

	c = 0
	s = 0
	v1 = []

	for i in range(n):
		# Current sum
		s += a[i]

		# Push the subsequence
		v1.append(a[i])

		# Current count
		c = c + 1

		# Storing negative elements
		# in priority queue
		if a[i] < 0:
			v.put(a[i])

		# If sum is less than zero
		# than subtract largest
		# negative number from left
		# and decrease the count
		if (s < 0):
			t = v.get()
			s = s-t
			# Erase the added vector
			v1.remove(t)

			c = c - 1

	# Largest subsequence
	for i in range(len(v1)):
		print(v1[i], end = " ")

# Driver Code
arr = [-3, -3, -7, -7, -1, -7,
	3, 3, -2, -1, 0, -7]

N = len(arr)

# Function Call
FindMaxSubsequence(arr, N)

# This code is contributed by Potta Lokesh
