# Python3 program to implement
# the above approach

# Function to count the maximum
# number of subarrays with sum K
def CtSubarr(arr, N, K):

	# Stores all the distinct
	# prefixSums obtained
	st = set()

	# Stores the prefix sum
	# of the current subarray
	prefixSum = 0

	st.add(prefixSum)

	# Stores the count of
	# subarrays with sum K
	res = 0

	for i in range(N):
		prefixSum += arr[i]

		# If a subarray with sum K
		# is already found
		if((prefixSum - K) in st):

			# Increase count
			res += 1

			# Reset prefix sum
			prefixSum = 0

			# Clear the set
			st.clear()
			st.add(0)

		# Insert the prefix sum
		st.add(prefixSum)

	return res

# Driver Code
arr = [ -2, 6, 6, 3, 5, 4, 1, 2, 8 ]
N = len(arr)
K = 10

# Function call
print(CtSubarr(arr, N, K))


