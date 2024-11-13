# Python3 program for the above approach

# Function to count the minimum replacements
# required to make the sum of equidistant
# array elements from the end equal
def minReplacements(nums, k):

	# Store the size of nums array
	N = len(nums)

	# Initialize an auxiliary array
	memo = [0]*(k * 2 + 2)

	# Iterate nums in range[0, N/2-1]
	for i in range(N//2):

		# Store the left element and
		# the right element
		l, r = nums[i], nums[N - 1 - i]

		# Decrement memo[min(l, r) + 1] by 1
		memo[min(l, r) + 1] -= 1

		# Decrement memo[l + r] by 1
		memo[l + r] -= 1

		# Increment memo[l + r + 1] by 1
		memo[l + r + 1] += 1

		# Increment memo[max(l, r) + k + 1] by 1
		memo[max(l, r) + k + 1] += 1

	# Store the minimum number of moves
	ans = N
	curr = N

	# Find the prefix sum of memo[]
	for i in range(2, 2 * k + 1):
		curr += memo[i]

		# Update ans
		ans = min(ans, curr)

	# Prthe answer
	print (ans)

# Driver Code
if __name__ == '__main__':
	arr =[1, 2, 4, 3]
	K = 4

	# Function Call
	minReplacements(arr, K)
