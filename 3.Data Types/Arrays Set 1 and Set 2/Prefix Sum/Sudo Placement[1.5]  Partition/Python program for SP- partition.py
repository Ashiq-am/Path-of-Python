# Python program for SP- partition

# Function to find the partition
def partition(a: list, n: int):
	mpp = dict()

	# mark the last occurrence of every element
	for i in range(n):
		mpp[a[i]] = i

	# calculate the prefix sum
	preSum = [0] * n
	preSum[0] = a[0]
	for i in range(1, n):
		preSum[i] = preSum[i - 1] + a[i]

	# calculate the suffix sum
	sufSum = [0] * n
	sufSum[n - 1] = a[n - 1]
	for i in range(n - 2, -1, -1):
		sufSum[i] = sufSum[i + 1] + a[i]

	# Check if partition is possible
	possible = False

	# Stores the absolute difference
	ans = int(1e18)

	# stores the last index till
	# which there can not be any partition
	count = 0

	# Stores the partition
	index = -1

	# Check if partition is possible or not
	# donot check for the last element
	# as partition is not possible
	for i in range(n - 1):

		# takes an element and checks it last occurrence
		# stores the maximum of the last occurrence
		# where partition can be done
		count = max(count, mpp[a[i]])

		# if partition is possible
		if count == i:

			# partition is possible
			possible = True

			# stores the left array sum
			sumleft = preSum[i]

			# stores the right array sum
			sumright = sufSum[i + 1]

			# check if the difference is minimum
			if abs(sumleft - sumright) < ans:
				ans = abs(sumleft - sumright)
				index = i + 1

	# is partition is possible or not
	if possible:
		print("%d.5" % index)
	else:
		print("-1")

# Driver Code
if __name__ == "__main__":

	a = [1, 2, -1, 2, 3]
	n = len(a)

	partition(a, n)
