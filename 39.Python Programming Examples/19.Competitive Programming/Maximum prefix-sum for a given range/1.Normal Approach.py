def ans(arr, l, r):
	# Calculate prefix sum for current query
	prefix_sum = 0
	max_prefix_sum = float('-inf')
	for i in range(l, r+1):
		prefix_sum += arr[i]
		max_prefix_sum = max(max_prefix_sum, prefix_sum)
	# returning the maximum prefix sum for current query
	return max_prefix_sum


if __name__ == '__main__':
	# given array for the question.
	arr = [-1, 2, 3, -5]
	# passing the first querry to the function.
	print(ans(arr, 0, 3))
	# passing the 2nd querry to the function.
	print(ans(arr, 1, 3))
