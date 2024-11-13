# Python3 program to find floor value
# of mean in range l to r
import math as mt

MAX = 1000005
prefixSum = [0 for i in range(MAX)]

# To calculate prefixSum of array
def calculatePrefixSum(arr, n):

	# Calculate prefix sum of array
	prefixSum[0] = arr[0]

	for i in range(1,n):
		prefixSum[i] = prefixSum[i - 1] + arr[i]

# To return floor of mean
# in range l to r
def findMean(l, r):

	if (l == 0):
		return mt.floor(prefixSum[r] / (r + 1))

	# Sum of elements in range l to
	# r is prefixSum[r] - prefixSum[l-1]
	# Number of elements in range
	# l to r is r - l + 1
	return (mt.floor((prefixSum[r] - prefixSum[l - 1]) / (r - l + 1)))

# Driver Code
arr = [1, 2, 3, 4, 5]

n = len(arr)

calculatePrefixSum(arr, n)
print(findMean(0, 2))
print(findMean(1, 3))
print(findMean(0, 4))
