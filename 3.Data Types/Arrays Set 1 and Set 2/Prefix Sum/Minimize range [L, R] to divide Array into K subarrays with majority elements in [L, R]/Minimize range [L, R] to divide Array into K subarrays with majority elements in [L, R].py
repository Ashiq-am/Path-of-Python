# python3 code for the above approach

# Function to minimize the range
# To divide the array arr
# Into k subarrays that has
# Number of elements in the range
# Greater than out of range
def find_minrange(arr, n, k):

	# Initialize the count vector
	# To store the frequencies
	# Of the elements
	count = [0 for _ in range(n + 1)]
	for x in arr:
		count[x] += 1

	# Initialize a vector prefix sum to
	# Store the number of elements till
	# That index
	prefixsum = [0 for _ in range(n + 1)]

	# Now traverse through from[1, n]
	# And store the count of elements till i
	for i in range(1, n+1):
		prefixsum[i] = prefixsum[i - 1] + count[i]

	low, high = 1, n

	# Initialize l, r to store the range
	l, r = 0, 0

	while (low <= high):
		# Initialize the mid
		mid = (low + high) // 2

		can = False

		# For each range size (mid)
		for i in range(1, n - mid + 1 + 1):

			# Count the number of elements
			# In the range [i, i+mid-1]
			# // And out of the range
			inrange = prefixsum[i + mid - 1] - prefixsum[i - 1]
			outrange = n - inrange

			# Check if the difference of inrange
			# And outrange is greater than
			# or equal to k
			if (inrange - outrange >= k):

				# Store the range
				# Since it is a possible range
				can = True
				l = i
				r = i + mid - 1
				break

		# If we have a possible range
		# Minimize it
		if (can):
			high = mid - 1

		else:
			low = mid + 1

	# Print the range
	print(f"{l} {r}")

# Driver Code
if __name__ == "__main__":

	# Initialize the array arr[]
	arr = [1, 2, 2, 2]
	K = 2
	N = len(arr)

	# Function call
	find_minrange(arr, N, K)
