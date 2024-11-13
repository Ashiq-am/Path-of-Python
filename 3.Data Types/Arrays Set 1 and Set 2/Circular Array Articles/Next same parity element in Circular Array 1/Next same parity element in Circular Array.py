# Python program for the above approach

# Function to return next same parity
def findElement(arr, n):
	# Initialize the vector with -1
	SPE = [-1] * n
	Next_Even = None
	Next_Odd = None

	# To check if odd and even
	# are more than one or not
	Count_Even = 0
	Count_Odd = 0

	for i in range(2 * n - 1, -1, -1):

		# Duplicate array
		if (i >= n):
			if (arr[i % n] & 1):
				Next_Odd = arr[i % n]
				Count_Odd += 1
			else:
				Next_Even = arr[i % n]
				Count_Even += 1

		# Original array
		else:
			if (arr[i] & 1):
				if (Count_Odd > 1):
					SPE[i] = Next_Odd
					Next_Odd = arr[i]
			else:
				if (Count_Even > 1):
					SPE[i] = Next_Even
					Next_Even = arr[i]

	return SPE


# Driver Code

arr = [2, 4, 3, 6, 5]
N = len(arr)

# Function call
v = findElement(arr, N)
for i in v:
	print(i, end=" ")


# This code is contributed by Saurabh Jaiswal
