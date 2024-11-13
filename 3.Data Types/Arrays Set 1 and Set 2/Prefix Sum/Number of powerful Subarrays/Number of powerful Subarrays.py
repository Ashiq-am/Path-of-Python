import math

# Function to check if a number is power of two
def isPowerOfTwo(n):
	if n == 0:
		return False
	return (math.ceil(math.log2(n)) == math.floor(math.log2(n)))

# Function to calculate prefix sum of even numbers
def evenOccur(arr, n, prefixSum):
	if arr[0] % 2 == 0:
		prefixSum[0] = 1
	else:
		prefixSum[0] = 0

	for i in range(1, n):
		if arr[i] % 2 == 0:
			prefixSum[i] = prefixSum[i-1] + 1
		else:
			prefixSum[i] = prefixSum[i-1]

# Main function to find subarrays with power of two times even numbers
def findTwoPowerEven(arr, n):
	evenCnt = [0] * n
	evenOccur(arr, n, evenCnt)

	cnt = 0
	evenInRange = 0

	for i in range(n):
		for j in range(i, n):
			if i == 0:
				evenInRange = evenCnt[j]
				if isPowerOfTwo(evenInRange):
					cnt += 1
			else:
				evenInRange = evenCnt[j] - evenCnt[i-1]
				if isPowerOfTwo(evenInRange):
					cnt += 1

	print("Number of subarrays having power of two times even numbers:", cnt)

# Driver code
arr = [1, 2, 4, 2]
size = len(arr)
findTwoPowerEven(arr, size)
