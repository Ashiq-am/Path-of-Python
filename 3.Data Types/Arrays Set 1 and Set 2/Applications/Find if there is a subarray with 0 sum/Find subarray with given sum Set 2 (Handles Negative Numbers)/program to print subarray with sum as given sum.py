# Python3 program to print subarray
# with sum as given sum


# Returns true if the there is a subarray
# of arr[] with sum equal to 'sum' otherwise
# returns false. Also, prints the result */
def subArraySum(arr, n, sum):

	# Pick a starting point
	for i in range(n):
		curr_sum = 0
		# try all subarrays starting with 'i'
		for j in range(i, n):
			curr_sum += arr[j]
			if (curr_sum == sum):
				print("Sum found between indexes", i, "and", j)
				return

	print("No subarray found")


# Driver Code
arr = [15, 2, 4, 8, 9, 5, 10, 23]
n = len(arr)
sum = 23

# Function Call
subArraySum(arr, n, sum)
