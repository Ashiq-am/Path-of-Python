# Python3 Program to find sum of
# product of each element with
# each element after it

# Return sum of product of each
# element with each element after it
def findSumofProduct(arr, n):
	sum = [None for _ in range(n)]
	sum[n-1] = arr[n - 1]

	# finding suffix sum
	for i in range(n - 2, -1, -1):
		sum[i] = sum[i + 1] + arr[i]

	# finding the sum of product of
	# each element with suffix sum.
	res = 0
	for i in range(n - 1):
		res += sum[i + 1] * arr[i]
	return res

# Driver Code
arr = [9, 3, 4, 2]
n = len(arr)
print(findSumofProduct(arr, n)) 
