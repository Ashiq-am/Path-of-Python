# Python 3 Program to find sum of
# product of each element
# with each element after it

# Return sum of product
# of each element with
# each element after it
def findSumofProduct(arr, n):
	suffix_sum = arr[n - 1]

	# Finding product of array
	# elements and suffix sum.
	res = 0
	for i in range(n - 2, -1, -1):

		res += (suffix_sum * arr[i])

		# finding suffix sum
		suffix_sum += arr[i]

	return res

# Driver Code
arr = [9, 3, 4, 2]
n = len(arr)
print(findSumofProduct(arr, n))
