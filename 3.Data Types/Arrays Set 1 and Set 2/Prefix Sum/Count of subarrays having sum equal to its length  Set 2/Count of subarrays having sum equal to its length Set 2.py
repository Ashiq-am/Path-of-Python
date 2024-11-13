# Python3 program for the above approach
from collections import defaultdict

# Function that counts the subarrays
# with sum of its elements as its length
def countOfSubarray(arr, N):

	# Store count of elements upto
	# current element with length i
	mp = defaultdict(lambda : 0)

	# Stores the final count of subarray
	answer = 0

	# Stores the prefix sum
	sum = 0

	# If size of subarray is 1
	mp[1] += 1

	# Iterate the array
	for i in range(N):

		# Find the sum
		sum += arr[i]
		answer += mp[sum - i]

		# Update frequency in map
		mp[sum - i] += 1

	# Print the total count
	print(answer)

# Driver code
if __name__ == '__main__':

	# Given array
	arr = [ 1, 0, 2, 1, 2, -2, 2, 4 ]

	# Size of the array
	N = len(arr)

	# Function Call
	countOfSubarray(arr, N)
