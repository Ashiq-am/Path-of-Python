# python3 program for the above approach
MXN = int(2e5)
precompute = [[0 for _ in range(MXN)] for _ in range(100)]

# To precompute count prefix sum of all
# possible remainders
def precomputation(arr, n, k):
	global precompute
	# Mark cell whose remainder is arr[i]%k
	for i in range(0, n):
		precompute[arr[i] % k][i] = 1

		# Take prefix sum for all rows
	for i in range(0, k):
		for j in range(1, n):
			precompute[i][j] += precompute[i][j - 1]

# Function to find the
# count of numbers for the queries
def findCount(arr, K, N, queries):
	global precompute
	res = []

	# Initialise matrix with 0

	# To calculate count of remainders
	precomputation(arr, N, K)
	for i in range(0, len(queries)):
		x = queries[i][0]
		l = queries[i][1]
		r = queries[i][2]
		if (x >= K):
			res.append(0)
			continue

		count = precompute[x][r] - precompute[x][l] + (arr[l] % K == x)
		res.append(count)

	return res

# Driver code
if __name__ == "__main__":

	arr = [15, 28, 72, 43, 20, 0, 97]

	K = 5
	N = len(arr)
	queries = [[3, 0, 3],
			[0, 0, 6],
			[6, 2, 4]]

	ans = findCount(arr, K, N, queries)
	for x in ans:
		print(x, end=" ")

	# This code is contributed by rakeshsahni
