# Python3 program for
# the above approach
MAX = 1000050

# Function to count
# total factors of N
def CountFactors(N):

	cnt = 0
	i = 1
	while i * i <= N:

		if (N % i == 0):
			if (N // i == i):
				cnt += 1
			else:
				cnt += 2
		i += 1

	# Return the count
	return cnt

# Function to search lowest N
# such that the given condition
# is satisfied
def minN(X):

	i = 1
	total = 0

	while (1):

		# Add the count of total factor
		# of i to variable total
		total = total + CountFactors(i)

		# If total count is greater than
		# equal to N, then return i
		if (total >= X):
			return i
		i += 1

# Driver Code
if __name__ == "__main__":

	# Given sum
	X = 10

	# Function Call
	print( minN(X))


