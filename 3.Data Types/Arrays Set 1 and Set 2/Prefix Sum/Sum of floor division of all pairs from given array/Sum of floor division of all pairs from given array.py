# Python3 program to implement
# the above approach

# Stores the maximum value of
# an array element
N = 10**5

# Function to find the sum of
# floor(a[i]/a[j]) of all pairs (i, j)
def getFloorSum(arr, n):

	# Stores frequency of
	# array element
	freq = [ 0 for i in range(N + 1)]

	# Stores prefix sum
	# array of frequency[]
	preFreq = [ 0 for i in range(N + 1)]

	# Traverse the array
	for i in range(n):

		# Update frequency
		# of arr[i]
		freq[arr[i]] += 1

	# Compute the prefix sum
	# of frequency[]
	for i in range(1, N):
		preFreq[i] = preFreq[i - 1] + freq[i]

	# Stores the sum of floor(a[i]/a[j])
	# of all pairs (i, j)
	ans = 0

	# Iterate over the range [1, Max]
	for i in range(1, N + 1):

		# Find the count of numbers in
		# the range [i * K, i * (K + 1))
		# and update the result
		for j in range(i, N + 1, i):

			# Stores count of numbers
			# in range[j - i - 1, j - 1]
			X = (preFreq[j - 1] - preFreq[j - i - 1])

			# Update ans
			ans += X * (j // i - 1) * freq[i]

	# Prthe answer
	print(ans)

# Driver Code
if __name__ == '__main__':

	# Given array
	arr = [1, 2, 3]

	# Stores the size of array
	n = len(arr)

	getFloorSum(arr, n)
