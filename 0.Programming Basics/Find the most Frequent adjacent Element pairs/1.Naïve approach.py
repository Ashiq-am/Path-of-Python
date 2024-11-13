# Python code for the above approach
def findMostFrequentPair(nums):
	maxFrequency = 0
	mostFrequentPair = []

	# Initialize the frequency to 1
	# for the current pair
	for i in range(len(nums) - 1):
		currentPairFrequency = 1
		for j in range(i + 1, len(nums)):

			# Increment the
			# frequency if the
			# pair matches.
			if nums[i] == nums[j] and i + 1 < len(nums) and j + 1 < len(nums) and nums[i + 1] == nums[j + 1]:
				currentPairFrequency += 1

		if currentPairFrequency > maxFrequency:
			maxFrequency = currentPairFrequency
			mostFrequentPair = [nums[i], nums[i + 1]]

	return mostFrequentPair


# Drivers code
arr = [1, 2, 2, 3, 2, 3, 4, 4, 4, 4]
result = findMostFrequentPair(arr)

# Function Call
print("Most Frequent Pair: {", result[0], ", ", result[1], "}")

# This code is contributed by Sakshi
