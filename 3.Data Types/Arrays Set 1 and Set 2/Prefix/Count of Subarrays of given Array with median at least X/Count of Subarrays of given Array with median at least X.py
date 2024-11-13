# python3 code to implement the above approach
import bisect

# Function to to find the Number of
# subarrays with median greater than
# or equal to X.
def findNumberOfSubarray(arr, n, X):

	# Build new array by comparing it with X
	new_array = [0 for _ in range(n)]

	for i in range(0, n):
		if (arr[i] >= X):
			new_array[i] = 1

		else:
			new_array[i] = -1

	# Build new array in which
	# at i-th index, Sum of first i elements
	# are stored
	pref_sum = [0 for _ in range(n)]
	pref_sum[0] = new_array[0]
	for i in range(1, n):
		pref_sum[i] = pref_sum[i - 1] + new_array[i]

	# Store the answer
	# Using long long because
	# it can exceed the storage limit of int
	ans = 0

	# For storing already traversed values
	s = set()
	s.add(0)

	# Iterating forwards from 0 to n-1.
	for i in range(0, n):

		less_than = bisect.bisect_left(
			sorted(s), pref_sum[i]+1, lo=0, hi=len(s))
		if pref_sum[i] + 1 in s:
			less_than += 1
		ans += less_than
		s.add(pref_sum[i])

	return ans

# Driver Code
if __name__ == "__main__":

	N, X = 4, 4
	arr = [5, 2, 4, 1]

	# Function call
	ans = findNumberOfSubarray(arr, N, X)
	print(ans)

	# This code is contributed by rakeshsahni
