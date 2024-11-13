# python3 code to implement the approach

# Function to count the number of elements
# that occur before any of the element
# present in its prefix in array A[]
def InvalidOrder(a, b, n):

	i, j, temp, validcount = 0, 0, 0, 0

	# Loop to count the elements
	# that are in valid order
	while (i < n and j < n):
		temp = j
		while (temp < n and a[i] != b[temp]):
			temp += 1

		if (temp != n):

			validcount += 1
			j = temp + 1

		i += 1

	# Return the answer
	return (n - validcount)

# Driver code
if __name__ == "__main__":

	A = [3, 5, 1, 2, 4]
	B = [4, 3, 1, 5, 2]
	N = len(A)

	# Function call
	print(InvalidOrder(A, B, N))

	# This code is contributed by rakeshsahni
