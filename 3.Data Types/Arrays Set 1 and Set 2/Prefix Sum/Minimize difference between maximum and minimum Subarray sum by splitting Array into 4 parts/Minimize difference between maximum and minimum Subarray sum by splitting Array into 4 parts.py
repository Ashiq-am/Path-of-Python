# Python3 code to implement the approach

# Function to find the minimum difference
# between maximum and minimum subarray sum
# after dividing the array into 4 subarrays
def minSum(v, n):
	a = [0]

	# Precompute the prefix sum
	for i in range(1, n + 1):
		a.append(a[-1] + v[i - 1])

	# Initialize the ans with large value
	ans = 10 ** 18

	# There are total four parts means 3 cuts.
	# Here i, j, k represent those 3 cuts
	i = 1
	j = 2
	k = 3
	while (j < n):
		while (i + 1 < j and abs(a[j] - 2 * a[i]) > abs(a[j] - 2 * a[i + 1])):
			i += 1
		while (k + 1 < n and abs(a[n] + a[j] - 2 * a[k]) > abs(a[n] + a[j] - 2 * a[k + 1])):
			k += 1
		ans = min(ans, max([a[i], a[j] - a[i], a[k] - a[j], a[n] - a[k]]
						) - min([a[i], a[j] - a[i], a[k] - a[j], a[n] - a[k]]))
		j += 1

	return ans

# Driver Code
arr = [3, 2, 4, 1, 2]
N = len(arr)

# Function call
print(minSum(arr, N))

# this code is contributed by phasing17
