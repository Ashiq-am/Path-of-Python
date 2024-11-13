# Python3 program for the
# above approach

# Function to calculate
# Bitwise OR of sums of
# all subsequences
def findOR(nums, N):

	# Stores the prefix
	# sum of nums[]
	prefix_sum = 0

	# Stores the bitwise OR of
	# sum of each subsequence
	result = 0

	# Iterate through array nums[]
	for i in range(N):

		# Bits set in nums[i] are
		# also set in result
		result |= nums[i]

		# Calculate prefix_sum
		prefix_sum += nums[i]

		# Bits set in prefix_sum
		# are also set in result
		result |= prefix_sum

	# Return the result
	return result

# Driver Code
if __name__ == "__main__":

	# Given array arr[]
	arr = [4, 2, 5]

	N = len(arr)

	# Function Call
	print(findOR(arr, N))
