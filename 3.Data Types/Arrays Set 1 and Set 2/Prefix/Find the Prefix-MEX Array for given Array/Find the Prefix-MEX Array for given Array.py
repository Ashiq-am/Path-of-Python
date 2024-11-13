# Python code to implement the approach

# Function to fint the prefix MEX
# for each array element
def Prefix_Mex(A, n):
	# Maximum element in vector A
	mx_element = max(A)
	# Store all number from 0
	# to maximum element + 1 in a set
	s = {}
	for i in range(mx_element+2):
		s[i] = True

	# Loop to calculate Mex for each index
	B = [0]*n
	for i in range(n):
		# Checking if A[i] is present in set
		# If present then we erase that element
		if A[i] in s.keys():
			del s[A[i]]
		# Store the first element of set
		# in vector B as Mex of prefix vector
		B[i] = int(list(s.keys())[0])
		# Return the list B
	return B


# Driver code
if __name__ == "__main__":
	A = [1, 0, 2, 4, 3]
	N = len(A)

	# Function call
	B = Prefix_Mex(A, N)

	# Print the prefix MEX array
	for i in range(N):
		print(B[i], end=" ")

# This code is contributed by Rohit Pradhan
