# Python program for the above approach:
def subarray_sum(nums, k):

	# Create a dictionary to
	# store the residual values
	# and their indices
	seen = {0: -1}

	# Initialize the prefix sum
	prefix_sum = 0

	for i, num in enumerate(nums):
		prefix_sum += num

		# Calculate the residual value
		residual = prefix_sum % k

		# If the same residual value has been
		# seen before and the subarray
		# size is at least 2
		if residual in seen and i - seen[residual] > 1:
			return True

		# If the residual value is
		# not seen before,
		# add it to the dictionary
		if residual not in seen:
			seen[residual] = i

	return False


# Test cases
print(subarray_sum([23, 2, 4, 6, 7], 6))
print(subarray_sum([23, 2, 6, 4, 7], 6))
