# Python code to implement the approach
def minCost(arr, cost, n):

	# Declare the maxSize varible to
	# store max upper number
	maxSize = 1000002

	total_cost_at_i = [0] * maxSize

	# Add the cost of all
	# similar elements
	for i in range(n):
		total_cost_at_i[arr[i]] += cost[i]

	# Declare the prefix and suffix arrays
	prefix = [0] * maxSize
	suffix = [0] * maxSize

	# Store the cost to convert all the
	# elements before i to i
	sum = 0
	for i in range(1, maxSize):
		prefix[i] = prefix[i - 1] + sum
		sum = sum + total_cost_at_i[i]

	# Store the cost to convert all the
	# elements after i + 1 to i
	sum = 0
	for i in range(maxSize - 2, -1, -1):
		suffix[i] = suffix[i + 1] + sum
		sum = sum + total_cost_at_i[i]

	# Store the minimum cost in the
	# min_cost variable.
	min_cost = 1e9 + 7
	for i in range(maxSize):
		min_cost = min(min_cost, (prefix[i] + suffix[i]))

	return min_cost

# Driver code
arr = [1, 3, 5, 2]
cost = [2, 3, 1, 14]
N = len(arr)

# Function Call
print(minCost(arr, cost, N))

# This code is contributed by Samim Hossain Mondal.
