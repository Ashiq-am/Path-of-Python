# Python code to implement above approach

# Function to get get the maximum cost
def solve(arr):
	n = len(arr)
	left = [0]*(n)
	right = [0]*(n)
	stack = []

	# Calculate left array
	for i in range(n):
		curr = arr[i]
		while(stack and
			arr[stack[-1]] >= curr):
			stack.pop()

		# Case 1
		if (len(stack) == 0):
			left[i] = (i + 1)*(arr[i])

		# Case 2
		else:
			small_idx = stack[-1]
			left[i] = left[small_idx] \
					+ (i - small_idx)*(arr[i])
		stack.append(i)

	stack.clear()

	# Calculate suffix sum array
	for i in range(n-1, -1, -1):
		curr = arr[i]
		while(stack and
			arr[stack[-1]] >= curr):
			stack.pop()

		if (len(stack) == 0):
			right[i] = (n-i)*(arr[i])

		else:
			small_idx = stack[-1]
			right[i] = right[small_idx] \
					+ (small_idx - i)*(arr[i])

		stack.append(i)

	ans = 0

	for i in range(n):
		curr = left[i] + right[i] - arr[i]
		ans = max(ans, curr)

	return (ans)

# Driver code
if __name__ == "__main__":
	arr = [5, 1, 8]
	print(solve(arr))
