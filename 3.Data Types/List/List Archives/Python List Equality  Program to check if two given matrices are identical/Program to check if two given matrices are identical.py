# Function to check if two given matrices are identical

def identicalMatrices(A,B):

	if A==B:
		print ('Matrices are identical')
	else:
		print ('Matrices are not identical')

# Driver program
if __name__ == "__main__":
	A = [ [1, 1, 1, 1],
		[2, 2, 2, 2],
		[3, 3, 3, 3],
		[4, 4, 4, 4]]

	B = [ [1, 1, 1, 1],
		[2, 2, 2, 2],
		[3, 3, 3, 3],
		[4, 4, 4, 4]]
	identicalMatrices(A,B)
