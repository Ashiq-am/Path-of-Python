# Python 3 program for the above approach
from collections import defaultdict
import sys
import math

# Function to find the index of the
# array such that the count of prime
# numbers to its either ends are same


def findIndex(arr, N):

	# Store the maximum value in
	# the array
	maxValue = -sys.maxsize - 1

	# Traverse the array arr[]
	for i in range(N):
		maxValue = max(maxValue, arr[i])

	# / Stores all the numbers
	St = defaultdict(int)

	# Iterate over the range [1, Max]
	for i in range(1, maxValue + 1):

		# Increment the value of st[i]
		St[i] += 1

	# Removes 1 from the map St
	if (1 in St):
		St.pop(1)

	# Perform Sieve of Prime Numbers
	for i in range(2, int(math.sqrt(maxValue)) + 1):
		j = 2

		# While i*j is less than
		# the maxValue
		while ((i * j) <= maxValue):

			# If i*j is in map St
			if (i * j) in St:

				# Erase the value (i * j)
				St.pop(i * j)

			# Increment the value of j
			j += 1

	# Stores the count of prime from
	# index 0 to i
	LeftCount = 0

	# Stores the count of prime numbers
	Prefix = [0] * N

	# Traverse the array arr[]
	for i in range(N):

		Prefix[i] = LeftCount

		# If arr[i] is present in the
		# map st
		if (arr[i] in St):
			LeftCount += 1

	# Stores the count of prime from
	# index i to N-1
	RightCount = 0

	# Stores the count of prime numbers
	Suffix = [0] * N

	# Iterate over the range [0, N-1]
	# in reverse order
	for i in range(N - 1, -1, -1):

		Suffix[i] = RightCount

		# If arr[i] is in map st
		if arr[i] in St:
			RightCount += 1

	# Iterate over the range [0, N-1]
	for i in range(N):

		# If prefix[i] is equal
		# to the Suffix[i]
		if (Prefix[i] == Suffix[i]):
			return i

	# Return -1 if no such index
	# is present
	return -1


# Driver Code
if __name__ == "__main__":

	arr = [2, 3, 4, 7, 5, 10, 1, 8]
	N = len(arr)
	print(findIndex(arr, N))
