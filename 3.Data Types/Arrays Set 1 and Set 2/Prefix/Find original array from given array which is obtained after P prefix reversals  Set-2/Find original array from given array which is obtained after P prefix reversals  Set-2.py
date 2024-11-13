# python code to implement above approach

# Function to find the original array
def findOriginal(arr, N, P):

	original = [0 for _ in range(N)]

	# Loop to fill the original array
	for i in range(0, P):
		x = (P - i) // 2

		# If (P-i) is odd
		if ((P - i) % 2):
			original[i] = arr[x]

		# If (P-i) is even
		else:
			original[i] = arr[i + x]

	for i in range(P, N):
		original[i] = arr[i]

	# Print the original array
	for i in range(0, N):
		print(original[i], end=" ")

# Driver code
if __name__ == "__main__":

	N = 6
	P = 4
	arr = [4, 2, 1, 3, 5, 6]

	# Function call to get original array
	findOriginal(arr, N, P)

	# This code is contributed by rakeshsahni
