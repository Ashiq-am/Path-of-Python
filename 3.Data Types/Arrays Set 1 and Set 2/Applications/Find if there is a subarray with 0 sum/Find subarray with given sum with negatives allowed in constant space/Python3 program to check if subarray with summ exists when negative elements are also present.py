# Python3 program to check if subarray with summ
# exists when negative elements are also present

# Function to check if subarray with summ
# exists when negative elements are also present
def subArraySum(arr, n, summ):
	minEle = 10**9

	# Find minimum element in the array
	for i in range(n):
		minEle = min(arr[i], minEle)

	# Initialize curr_summ as value of
	# first element and starting poas 0
	curr_summ = arr[0] + abs(minEle)
	start = 0

	# Starting window length will be 1,
	# For generating new target summ,
	# add abs(minEle) to summ only 1 time
	targetSum = summ

	# Add elements one by one to curr_summ
	# and if the curr_summ exceeds the
	# updated summ, then remove starting element
	for i in range(1, n + 1):

		# If curr_summ exceeds the summ,
		# then remove the starting elements
		while (curr_summ - (i - start) * abs(minEle) >
					targetSum and start < i - 1):
			curr_summ = curr_summ - arr[start] - abs(minEle)
			start += 1

		# If curr_summ becomes equal to summ,
		# then return true
		if (curr_summ - (i - start) *
			abs(minEle) == targetSum):
			print("Sum found between indexes",
						start, "and", i - 1)
			return

		# Add this element to curr_summ
		if (i < n):
			curr_summ = curr_summ + arr[i] + abs(minEle)

	# If we reach here, then no subarray
	print("No subarray found")

# Driver Code
arr = [10, -12, 2, -2, -20, 10]
n = len(arr)

summ = -10

subArraySum(arr, n, summ) 
