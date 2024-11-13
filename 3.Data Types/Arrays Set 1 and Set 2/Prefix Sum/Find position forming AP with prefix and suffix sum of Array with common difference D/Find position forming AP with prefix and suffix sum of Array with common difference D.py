#Python program for the above approach

# Function to check if there is
# an element forming A.P. series
# having common difference d
def checkArray(arr, N, d):

	# If size of array is less than
	# three then return -1
	if (N < 3):
		return -1

	# Initialize the variables
	i = 0
	Sum = 0
	temp = 0

	# Calculate total sum of array
	for i in range (N):
		Sum += arr[i]

	if (Sum % 3 != 0):
		return 0

	# Calculate Middle element of A.P. series
	Mid = Sum / 3

	# Iterate over the range
	for i in range(1, N - 1):

		# Store the first element of A.P.
		# series in the variable temp
		temp += arr[i - 1]

		if (arr[i] == Mid):

			# Return position of middle element
			# of the A.P. series if the first
			# element is in A.P. with middle element
			# having common difference d
			if (temp == Mid - d):
				return i + 1

			# Else return 0
			else:
				return 0

	# If middle element is not found in arr[]
	return 0

# Driver Code
if __name__ == "__main__":

	arr = [ 4, 6, 20, 10, 15, 5 ]
	N = len(arr)
	D = 10

	# Function call
	print(checkArray(arr, N, D))
