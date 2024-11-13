# Python3 program for the above approach

# To store the prefix sum1 array
v = []

# Function for searching the
# lower bound of the subarray


def bin1(val, k, n):

	global v
	lo = 0
	hi = n
	mid = 0
	ans = -1

	# Iterate until low less
	# than equal to high
	while (lo <= hi):
		mid = lo + ((hi - lo) // 2)

		# For each mid finding sum1
		# of sub array less than
		# or equal to k
		if (v[mid] - val <= k):
			lo = mid + 1
			ans = mid
		else:
			hi = mid - 1

	# Return the final answer
	return ans

# Function to find the length of
# subarray with sum1 K


def findSubarraysum1K(arr, N, K):

	global v

	# Initialize sum1 to 0
	sum1 = 0
	v.append(0)

	# Push the prefix sum1 of the
	# array arr[] in prefix[]
	for i in range(N):
		sum1 += arr[i]
		v.append(sum1)

	l = 0
	ans = 0
	r = 0

	for i in range(len(v)):

		# Search r for each i
		r = bin1(v[i], K, N)

		# Update ans
		ans = max(ans, r - i)

	# Print the length of subarray
	# found in the array
	print(ans)


# Driver Code
if __name__ == '__main__':

	# Given array arr[]
	arr = [6, 8, 14, 9, 4, 11, 10]

	N = len(arr)

	# Given sum1 K
	K = 13

	# Function Call
	findSubarraysum1K(arr, N, K)
