# Function to find the maximum number of iterations
def helper(A):
	# Sort the array in descending order
	A.sort(reverse=True)

	# Find the minimum element and its position
	minimum = A[-1]
	pos = 0
	for i in range(len(A)):
		if A[i] == minimum:
			# The first position which is minimum
			pos = i
			break

	return minimum * len(A) + pos

# Driver Code
if __name__ == "__main__":
	N = 4
	A = [3, 0, 2, 1]

	# Function Call
	print(helper(A))
