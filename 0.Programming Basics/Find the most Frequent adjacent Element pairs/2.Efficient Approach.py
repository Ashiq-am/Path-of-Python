def find_most_frequent_pair(nums):
	pair_frequency = {}
	max_frequency = 0
	most_frequent_pair = []

	for i in range(len(nums) - 1):
		# Combine two adjacent elements into a single integer
		current_pair = (nums[i] << 16) | nums[i + 1]
		pair_frequency[current_pair] = pair_frequency.get(current_pair, 0) + 1

		if pair_frequency[current_pair] > max_frequency:
			max_frequency = pair_frequency[current_pair]
			most_frequent_pair = [nums[i], nums[i + 1]]

	return most_frequent_pair

# Driver code
arr = [1, 2, 2, 3, 2, 3, 4, 4, 4, 4]
result = find_most_frequent_pair(arr)

# Function call
print(f"Most Frequent Pair: {result}")
