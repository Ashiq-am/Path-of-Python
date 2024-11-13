# Python3 program for the above approach

# Function to maximize difference of
# the sum of absolute difference of
# an element with the rest of the
# elements in the array
def findMaxDifference(arr, n):

	# Sort the array in ascending order
	arr = sorted(arr)

	# Stores prefix sum at any instant
	Leftsum = 0

	# Store the total array sum
	Totalsum = 0

	# Initialize minimum and maximum
	# absolute difference
	Min, Max = 10**8, -10**8

	# Traverse the array to find
	# the total array sum
	for i in range(n):
		Totalsum += arr[i]

	# Traverse the array arr[]
	for i in range(n):

		# Store the number of
		# elements to its left
		leftNumbers = i

		# Store the number of
		# elements to its right
		rightNumbers = n - i - 1

		# Update the sum of elements
		# on its left
		Totalsum = Totalsum - arr[i]

		# Store the absolute difference sum
		sum = (leftNumbers * arr[i])- Leftsum + Totalsum - (rightNumbers * arr[i])

		# Update the Minimum
		Min = min(Min, sum)

		# Update the Maximum
		Max = max(Max, sum)

		# Update sum of elements
		# on its left
		Leftsum += arr[i]

	# Prthe result
	print (Max - Min)

# Driven Code
if __name__ == '__main__':
	arr = [1, 2, 4, 7]
	N = len(arr)
	findMaxDifference(arr, N)
