# Python code to implement the above approach

# Given mod number .
MOD = int(1e9 + 7)

# Function performing calculation


def countAndGood(n, arr):

	# Initializing preAnd .
	preAnd = (1 << 30) - 1

	# Precomputing the And of the array arr
	for i in range(n):
		preAnd &= arr[i]

		# Initializing cnt with 0
	cnt = 0

	# Counting the total number in arr which
	# are equal to preAnd
	for i in range(n):
		if preAnd == arr[i]:
			cnt += 1

	# Finding (cnt)P(cnt-2)
	ans = (cnt * (cnt - 1)) % MOD

	# Finding (n-2)!
	temp = 1
	for i in range(2, n - 2 + 1):
		temp = (temp * i) % MOD

	# Multiplying temp and ans
	ans = (ans * temp) % MOD

	# Returning ans variable
	return ans


# Driver Code
N = 4
arr = [1, 3, 5, 1]

# Function Call
print(countAndGood(N, arr))
# This Code is Contributed by Prasad Kandekar(prasad264)
