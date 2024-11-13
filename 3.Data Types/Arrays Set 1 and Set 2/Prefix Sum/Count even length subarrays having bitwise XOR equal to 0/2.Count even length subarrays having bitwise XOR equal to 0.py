# Python3 program to implement
# the above appraoch
M = 1000000

# Function to get the count
# of even length subarrays
# having bitwise xor 0
def cntSubXor(arr, N):

	# Stores prefix-xor of
	# the given array
	prefixXor = 0

	# Stores prefix-xor at
	# even index of the array.
	Even =[0] * M

	# Stores prefix-xor at
	# odd index of the array.
	Odd = [0] * M

	# Stores count of subarrays
	# that satisfy the condition
	cntSub = 0

	# length from 0 index
	# to odd index is even
	Odd[0] = 1

	# Traverse the array.
	for i in range(0, N):

		# Take prefix-xor
		prefixXor ^= arr[i]

		# If index is odd
		if (i % 2 == 1):

			# Calculate pairs
			cntSub += Odd[prefixXor]

			# Increment prefix-xor
			# at odd index
			Odd[prefixXor] += 1
		else:

			# Calculate pairs
			cntSub += Even[prefixXor]

			# Increment prefix-xor
			# at odd index
			Even[prefixXor] += 1
	return cntSub

# Driver Code
if __name__ == '__main__':

	arr = [2, 2, 3, 3,
		6, 7, 8]
	N = len(arr)
	print(cntSubXor(arr, N))


