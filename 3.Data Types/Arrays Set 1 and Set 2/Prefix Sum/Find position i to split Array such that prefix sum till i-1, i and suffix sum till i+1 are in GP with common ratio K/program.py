# python program for the above approach

# Function to check if there is
# an element forming G.P. series
# having common ratio k
def checkArray(arr, N, k):

		# If size of array is less than
		# three then return -1
	if (N < 3):
		return -1

		# Initialize the variables
	Sum = 0
	temp = 0

	# Calculate total sum of array
	for i in range(0, N):
		Sum += arr[i]

	R = (k * k + k + 1)

	if (Sum % R != 0):
		return 0

		# Calculate Middle element of G.P. series
	Mid = k * (Sum // R)

	# Iterate over the range
	for i in range(1, N-1):

				# Store the first element of G.P.
				# series in the variable temp
		temp += arr[i - 1]

		if (arr[i] == Mid):

						# Return position of middle element
						# of the G.P. series if the first
						# element is in G.P. of common ratio k
			if (temp == Mid // k):
				return i + 1

				# Else return 0
			else:
				return 0

		# if middle element is not found in arr[]
	return 0

# Driver Code
if __name__ == "__main__":

	# Given array
	arr = [5, 1, 4, 20, 6, 15, 9, 10]
	N = len(arr)
	K = 2

	print(checkArray(arr, N, K))
