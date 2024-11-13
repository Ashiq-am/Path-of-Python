def minOperation(s):
	# Storing prefixSum with index
	# of its first occurrence
	unmap = {}
	n = len(s)

	# For storing the prefix Sum
	# ending at ith index
	prefixSum = 0

	# For keeping the length of
	# the longest binary string where
	# the number of zeros and ones are equal
	result = 0

	# Iterate over the string
	for i in range(n):
		if s[i] == '1':
			prefixSum += 1
		else:
			prefixSum -= 1

		if prefixSum == 0:
			result = max(result, i + 1)

		# Check if prefixSum has
		# previously occurred or not
		if prefixSum in unmap:
			# Update the result with
			# this valid substring
			result = max(result, i - unmap[prefixSum])
		else:
			# Store this prefixSum has
			# occurred at ith index
			# in the map.
			unmap[prefixSum] = i

	# Return the remaining length
	# other than the longest
	# valid substring.
	return n - result

# Driver code
if __name__ == "__main__":
	S = "0111000"

	# Function call
	result = minOperation(S)
	print(result)
