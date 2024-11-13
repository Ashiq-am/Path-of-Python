def solve(N, arr, X, Y):
	# Sort the array in non-decreasing order
	arr.sort(reverse=True)

	# Calculate prefix sums
	for i in range(1, N):
		arr[i] += arr[i - 1]

	# Initialize answer
	ans = -1_000_000_000

	# Iterate over possible values of i
	for i in range(X + 1):
		if i == 0:
			curr = arr[N - 1] - 2 * (arr[min(i + Y - 1, N - 1)])
			ans = max(ans, curr)
		else:
			curr = arr[N - 1] - 2 * arr[min(i + Y - 1, N - 1)] + arr[i - 1]
			ans = max(ans, curr)

	# Output the answer
	print(ans)

# Main function
if __name__ == "__main__":
	# Input variables: N, X, Y
	N, X, Y = 8, 5, 3

	# List to store array elements
	arr = [5, 5, 3, 3, 3, 2, 9, 9]
	solve(N, arr, X, Y)

#This code is contributed by rohit singh
