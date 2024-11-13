# Python implementation for the above approach
from queue import PriorityQueue

# Function to calculate longest length
# of subsequence such that its prefix sum
# at every element stays greater than zero
def maxScore(arr, N):

	# Variable to store the answer
	score = 0

	# Min heap implementation
	# using a priority queue
	pq = PriorityQueue()

	# Variable to store the sum
	sum = 0
	for i in range(N) :

		# Add the current element
		# to the sum
		sum += arr[i]

		# Push the element in
		# the min-heap
		pq.put(arr[i])

		# If the sum becomes less than
		# zero pop the top element of
		# the min-heap and subtract it
		# from the sum
		if (sum < 0):
			a = pq.queue[0]
			sum -= a
			pq.get()

	# Return the answer
	return pq.qsize()

# Driver Code
arr = [ -2, 3, 3, -7, -5, 1 ]
N = len(arr)

print(maxScore(arr, N))
