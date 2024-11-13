# Python 3 program for the above approach

# Function to check whether
# only one bit is set or not
def check(x):
	if (((x) & (x - 1)) == 0):
		return 1
	return 0

# Function to perform Range-query
def query(l, r, pre):
	if (l == 0):
		return pre[r]
	else:
		return pre[r] - pre[l - 1]

# Function to count array elements with a
# single set bit for each range in a query
def countInRange(arr, N, queries, Q):

	# Initialize array for Prefix sum
	pre = [0] * N
	pre[0] = check(arr[0])
	for i in range(1, N):
		pre[i] = pre[i - 1] + check(arr[i])
	c = 0
	while (Q > 0):
		l = queries[0]
		r = queries[1]
		c += 1
		print(query(l, r, pre), end=" ")
		Q -= 1


# Driver Code
if __name__ == "__main__":

	# Given array
	arr = [12, 11, 16, 8, 2, 5, 1, 3, 256, 1]

	# Size of the array
	N = len(arr)

	# Given queries
	queries = [[0, 9], [4, 9]]

	# Size of queries array
	Q = len(queries)

	countInRange(arr, N, queries, Q)

	# this code is contributed by chitranayal.
