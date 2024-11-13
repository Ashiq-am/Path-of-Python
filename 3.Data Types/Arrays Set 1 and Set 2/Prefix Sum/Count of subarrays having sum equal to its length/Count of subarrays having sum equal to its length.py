# Python3 program for the above approach
from collections import defaultdict

# Function that counts the subarrays
# with sum of its elements as its length
def countOfSubarray(arr, N):

	# Decrementing all the elements
	# of the array by 1
	for i in range(N):
		arr[i] -= 1

	# Making prefix sum array
	pref = [0] * N
	pref[0] = arr[0]

	for i in range(1, N):
		pref[i] = pref[i - 1] + arr[i]

	# Declare map to store count of
	# elements upto current element
	mp = defaultdict(lambda : 0)
	answer = 0

	# To count all the subarrays
	# whose prefix sum is 0
	mp[0] += 1

	# Iterate the array
	for i in range(N):

		# Increment answer by count of
		# current element of prefix array
		answer += mp[pref[i]]
		mp[pref[i]] += 1

	# Return the answer
	return answer

# Driver Code

# Given array arr[]
arr = [ 1, 1, 0 ]
N = len(arr)

# Function call
print(countOfSubarray(arr, N))
