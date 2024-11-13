# python3 program to implement the approach

# Precompute for every array
def pre_compute(arr, K, mp):

	for i in range(0, K):

		# Size of ith row stored in n
		n = len(arr[i])
		mp[arr[i][0]] = min(
			(mp[arr[i][0]] if arr[i][0] in mp else 0) + 1, i + 1)

		# Precomputing ith row
		for j in range(1, n):
			arr[i][j] += arr[i][j - 1]
			mp[arr[i][j]] = min((mp[arr[i][j]] if arr[i][j] in mp else 0) + 1,
								i + 1)

# Function to calculate minimum common sum
def min_common_sum(arr, K):

	mp = {}

	# Function call to precompute
	# every row in arr
	pre_compute(arr, K, mp)

	for i in range(0, len(arr[0])):
		if (mp[arr[0][i]] == K):
			return arr[0][i]

	return -1

# Driver code
if __name__ == "__main__":

	K = 3

	# All k arrays are stored using 2D vector
	arr = [[5, 2, 4], [1, 4, 1, 1], [2, 3]]

	ans = min_common_sum(arr, K)
	print(ans)

	# This code is contributed by rakeshsahni
