# Python3 program for
# the above approach

# Function to prthe
# required resultant array
def sumOfKElements(arr, n, k):

	# Reverse the array
	rev = False

	if (k < 0):

		rev = True
		k *= -1
		l = 0
		r = n - 1

		# Traverse the range
		while (l < r):
			tmp = arr[l]
			arr[l] = arr[r]
			arr[r] = tmp
			l += 1
			r -= 1

	# Store prefix sum
	dp = [0] * n
	dp[0] = arr[0]

	# Find the prefix sum
	for i in range(1, n):
		dp[i] += dp[i - 1] + arr[i]

	# Store the answer
	ans = [0] * n

	# Calculate the answers
	for i in range(n):
		if (i + k < n):
			ans[i] = dp[i + k] - dp[i]
		else:

			# Count of remaining
			# elements
			x = k - (n - 1 - i)

			# Add the sum of
			# all elements y times
			y = x // n

			# Add the remaining
			# elements
			rem = x % n

			# Update ans[i]
			ans[i] = (dp[n - 1] - dp[i] +
					y * dp[n - 1] +
					(dp[rem - 1]
					if rem - 1 >= 0
					else 0))

	# If array is reversed
	# print ans in reverse
	if (rev):
		for i in range(n - 1, -1, -1):
			print(ans[i], end = " ")

	else:
		for i in range(n):
			print(ans[i], end = " ")

# Driver Code
if __name__ == '__main__':

	# Given array arr
	arr = [4, 2, -5, 11]

	N = len(arr)

	# Given K
	K = 3

	# Function
	sumOfKElements(arr, N, K)


