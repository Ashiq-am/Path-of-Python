# Python3 implementation of the given approach

# This function returns true if the array
# can be divided into three equal sum segments
def equiSumUtil(arr, pos1, pos2):

	n = len(arr)

	# Prefix Sum Array
	pre = [0] * n
	sum = 0
	for i in range(n):
		sum += arr[i]
		pre[i] = sum

	# Suffix Sum Array
	suf = [0] * n
	sum = 0
	for i in range(n - 1, -1, -1):
		sum += arr[i]
		suf[i] = sum

	# Stores the total sum of the array
	total_sum = sum

	i = 0
	j = n - 1
	while (i < j - 1):

		if (pre[i] == total_sum // 3):
			pos1 = i

		if (suf[j] == total_sum // 3):
			pos2 = j

		if (pos1 != -1 and pos2 != -1):

			# We can also take pre[pos2 - 1] - pre[pos1] ==
			# total_sum / 3 here.
			if (suf[pos1 + 1] -
				suf[pos2] == total_sum // 3):
				return [True, pos1, pos2]
			else:
				return [False, pos1, pos2]

		if (pre[i] < suf[j]):
			i += 1
		else:
			j -= 1

	return [False, pos1, pos2]

def equiSum(arr):

	pos1 = -1
	pos2 = -1
	ans = equiSumUtil(arr, pos1, pos2)
	pos1 = ans[1]
	pos2 = ans[2]
	if (ans[0]):
		print("First Segment : ", end = "")
		for i in range(pos1 + 1):
			print(arr[i], end = " ")

		print("")

		print("Second Segment : ", end = "")
		for i in range(pos1 + 1, pos2):
			print(arr[i], end = " ")

		print("")

		print("Third Segment : ", end = "")
		for i in range(pos2, len(arr)):
			print(arr[i], end = " ")

		print("")
	else:
		print("Array cannot be divided into","three equal sum segments")

# Driver Code
arr = [1, 3, 6, 2, 7, 1, 2, 8 ]
equiSum(arr)


