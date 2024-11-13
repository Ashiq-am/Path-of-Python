# Python3 program to implement
# the above approach

# Function to perform XOR in
# the range [lo, hi]
def findxor(temp, N, lo, hi, val):

	temp[lo] ^= val
	if (hi != N - 1):
		temp[hi + 1] ^= val

# Function to generate Prefix
# Xor Array
def updateArray(temp, N):

	for i in range(1, N):
		temp[i] ^= temp[i - 1]

# Function to perform each Query
# and print the final array
def xorQuery(arr, n, Q):

	temp =[0] * n

	# Perform each Query
	for i in range(len(Q)):
		findxor(temp, n, Q[i][0] - 1,
						Q[i][1] - 1,
						Q[i][2])

	# Modify the array
	updateArray(temp, n)

	# Print the final array
	for i in range(n):
		print((arr[i] ^ temp[i]), end = " ")

# Driver Code
if __name__ == "__main__":

	arr = [ 2, 3, 6, 5, 4 ]
	n = len(arr)
	Q = [ [ 1, 3, 2 ],
		[ 2, 4, 4 ] ]

	xorQuery(arr, n, Q)

# This code is contributed by chitranayal
