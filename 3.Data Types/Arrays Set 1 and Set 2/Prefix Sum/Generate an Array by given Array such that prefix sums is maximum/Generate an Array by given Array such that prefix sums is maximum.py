# python code to implement the approach

def maxPrefix(A):
	# 1st pointer
	leftEnd = 0

	# List for temporary storing same parity sub-arrays
	lst = []
	while leftEnd < len(A):

		# Variable to hold parity of current sub-array
		# For odd parity = 1, for even parity = 0
		parity = 0 if A[leftEnd] % 2 == 0 else 1

		# 2nd pointer
		rightEnd = leftEnd
		lst.append(A[leftEnd])

		while (rightEnd < len(A) - 1) and (A[rightEnd + 1] % 2 == parity):
			rightEnd += 1
			lst.append(A[rightEnd])

		# Sorting the list in reverse order
		lst.sort(reverse=True)

		# Counter variable for iterating from starting on the list
		counter = 0

		# Loop for initializing elements from the list to A[]
		for i in range(leftEnd, leftEnd + len(lst)):
			A[i] = lst[counter]
			counter += 1

		# Clearing all the elements from the list
		lst.clear()

		# Updating the value of the 1st pointer
		leftEnd = rightEnd + 1

	# Printing A[]
	print(A)


# Driver code
A = [1, 5, 7]
maxPrefix(A)
