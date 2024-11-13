# Python3 program for largest sum
# contiguous subarray by adding S
# exactly at K different positions

# Function to find the largest sum
# subarray after adding s at k
# different positions for k from [0, n]
import sys

def find_maxsum_subarray(arr, n, s):
	msum = [0]*n
	prefix_sum = [0]*(n+1)

	# Find the prefix sum
	for i in range(n):
		if (i == 0):
			prefix_sum[i + 1] = arr[i]
		else:
			prefix_sum[i + 1] = arr[i] + prefix_sum[i]

	# For each subarray of size i
	# find the maximum sum
	for i in range(n):

		mx_sum = -sys.maxsize-1

		# Check for every subarray of size i
		for j in range(n - i):
			mx_sum = max(mx_sum,prefix_sum[j + i + 1]-prefix_sum[j])

		# Store the maximum sub array sum for
		# each subarray of size i in msum array
		msum[i] = mx_sum

	# For every k check the max sum
	# subarray by adding s
	# at k different positions
	for k in range(n+1):

		mx_sum = 0

		# For each maxsum of subarray of size i
		# check by s at k positions
		# find the maximum sum
		# after adding s at k positions
		for i in range(n):
			mx_sum = max(mx_sum,msum[i]+ min(i + 1, k) * s)

		# For each k
		# print the maximum subarray sum
		print(mx_sum,end=" ")

# Driver code
arr = [ 4, 1, 3, 2 ]
n = len(arr)
s = 2
find_maxsum_subarray(arr, n, s)
