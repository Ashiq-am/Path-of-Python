# Python3 program for the above approach

# Function to find the NGE
def printNGE(A, n):

	# Formation of cicular array
	arr = [0] * (2 * n)

	# Append the given array
	# element twice
	for i in range(2 * n):
		arr[i] = A[i % n]

	# Iterate for all the
	# elements of the array
	for i in range(n):

		# Initialise NGE as -1
		next = -1

		for j in range(i + 1, 2 * n):

			# Checking for next
			# greater element
			if(arr[i] < arr[j]):
				next = arr[j]
				break

		# Print the updated NGE
		print(next, end = ", ")

# Driver code
if __name__ == '__main__':

	# Given array arr[]
	arr = [ 1, 2, 1 ]

	N = len(arr)

	# Function call
	printNGE(arr, N)


