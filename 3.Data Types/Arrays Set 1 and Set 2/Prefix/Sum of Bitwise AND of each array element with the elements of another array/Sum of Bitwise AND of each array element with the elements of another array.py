# Python3 program for the above approach

# Function to compute the AND sum
# for each element of an array
def Bitwise_AND_sum_i(arr1, arr2, M, N):

	# Declaring an array of
	# size 32 for storing the
	# count of each bit
	frequency = [0]*32

	# Traverse the array arr2[]
	# and store the count of a
	# bit in frequency array
	for i in range(N):

		# Current bit position
		bit_position = 0
		num = arr1[i]

		# While num is greater
		# than 0
		while (num):

			# Checks if ith bit is
			# set or not
			if (num & 1):

				# Increment the count of
				# bit by one
				frequency[bit_position] += 1

			# Increment the bit position
			# by one
			bit_position += 1

			# Right shift the num by one
			num >>= 1

	# Traverse in the arr2[]
	for i in range(M):
		num = arr2[i]

		# Store the ith bit
		# value
		value_at_that_bit = 1

		# Total required sum
		bitwise_AND_sum = 0

		# Traverse in the range [0, 31]
		for bit_position in range(32):

			# Checks if current bit is set
			if (num & 1):

				# Increment the bitwise sum
				# by frequency[bit_position]
				# * value_at_that_bit
				bitwise_AND_sum += frequency[bit_position] * value_at_that_bit

			# Right shift num by one
			num >>= 1

			# Left shift vale_at_that_bit by one
			value_at_that_bit <<= 1

		# Print sum obtained for ith
		# number in arr1[]
		print(bitwise_AND_sum, end = " ")
	return

# Driver Code
if __name__ == '__main__':

	# Given arr1[]
	arr1 = [1, 2, 3]

	# Given arr2
	arr2 = [1, 2, 3]

	# Size of arr1[]
	N = len(arr1)

	# Size of arr2[]
	M = len(arr2)

	# Function Call
	Bitwise_AND_sum_i(arr1, arr2, M, N)

# This code is contributed by mohit kumar 29
