# Python3 program to find fibonacci sum of
# subarray where all elements <= k

from bisect import bisect

# Helper function that multiplies 2 matrices
# F and M of size 2*2, and puts the multiplication
# result back to F
def multiply(F, M):
	x = F[0][0] * M[0][0] + F[0][1] * M[1][0]
	y = F[0][0] * M[0][1] + F[0][1] * M[1][1]
	z = F[1][0] * M[0][0] + F[1][1] * M[1][0]
	w = F[1][0] * M[0][1] + F[1][1] * M[1][1]

	F[0][0] = x
	F[0][1] = y
	F[1][0] = z
	F[1][1] = w

# Helper function that calculates F
# raise to the power n and puts the
# result in F
def power(F, n):
	M = [[1, 1], [1, 0]]

	# n - 1 times multiply the
	# matrix to [[1, 0], [0, 1]]
	for i in range(1, n):
		multiply(F, M)

# Returns the nth fibonacci number
def fib(n):
	F = [[1, 1], [1, 0]]
	if (n == 0):
		return 0
	power(F, n - 1)

	return F[0][0]


def findLessThanK(arr, n, k):
	# find first index which is > k
	# using bisect
	return (bisect(arr, k))

# Function to build Prefix Fibonacci Sum
def buildPrefixFibonacciSum(arr, n):
	# Allocate memory to prefix
	# fibonacci sum array
	prefixFibSum = [0]*n

	# Traverse the array from 0 to n - 1,
	# when at the ith index then we calculate
	# the a[i]th fibonacci number and calculate
	# the fibonacci sum till the ith index as
	# the sum of fibonacci sum till index i - 1
	# and the a[i]th fibonacci number
	for i in range(n):
		currFibNumber = fib(arr[i])
		if (i == 0):
			prefixFibSum[i] = currFibNumber
		else:
			prefixFibSum[i] = prefixFibSum[i - 1] + currFibNumber
	return prefixFibSum

# Return the answer for each query


def processQuery(arr, prefixFibSum, n, k):

	# index stores the index till where
	# the array elements are less than k
	lessThanIndex = findLessThanK(arr, n, k)

	if (lessThanIndex == 0):
		return 0
	return prefixFibSum[lessThanIndex - 1]


# Driver Code
if __name__ == '__main__':
	arr = [1, 2, 3, 4, 2, 7]
	n = len(arr)

	# sort the array arr
	arr.sort()

	# Build the prefix fibonacci sum array
	prefixFibSum = buildPrefixFibonacciSum(arr, n)

	# query array stores q queries
	query = [2, 6]
	q = len(query)

	for i in range(q):
		k = query[i]
		ans = processQuery(arr, prefixFibSum, n, k)

		print("Query {} : {}".format(i+1, ans))

# This code is contributed by Amartya Ghosh
