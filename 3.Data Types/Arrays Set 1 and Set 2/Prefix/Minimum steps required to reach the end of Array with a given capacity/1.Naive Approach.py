# python code for the above approach:

import bisect

def minSteps(arr, c):
	n = len(arr)

	# Find the size of the array
	pre = [0] * n

	# Declare a prefix sum list for storing the result beforehand
	pre[0] = arr[0]

	for i in range(1, n):
		pre[i] = pre[i - 1] + arr[i]

	# Fill the prefix sum list
	curr = 0
	sc = c
	ans = 0

	while True:
		ind = bisect.bisect_left(pre, sc)

		# Finding the lower bound using binary search and subtracting
		# the previously computed value
		if ind >= n:
			return ans + n

		# If the index goes beyond the array size, then return the size
		# summed up with array size
		elif pre[ind] == sc:
			# If the element at the prefix array is equal to the source, then
			# check if the index has reached the last element
			if ind == n - 1:
				return ans + n
			curr = ind
		else:
			curr = ind - 1

		sc = c + pre[curr]

		# Add prefix value at the current index to the source
		ans += 2 * (curr + 1)

# Drivers code
if __name__ == "__main__":
	v = [8, 8, 8, 8, 8]
	c = 10

	# Function Call
	print(minSteps(v, c))
