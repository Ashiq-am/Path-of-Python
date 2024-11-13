# python3 program for Generate permutation
# of length N such that sum of all prefix
# minimum of that permutation is Y.

# Find the value greedily for the
# current index as discussed in approach
def findValue(N, Y):
	return min(N, Y + 1 - N)

# Function to generate the permutation
def generatePermutation(N, Y):

	# Store the prefix minimum array first
	# then we will convert it to permutation
	ans = [0 for _ in range(N)]

	# If Y should belong to [N, (N*(N + 1)/2)],
	# otherwise we will print -1;
	if (Y < N or (2 * Y) > (N * (N + 1))):
		print(-1)
		return

	# Remaining elements to be taken
	s = set()

	for i in range(1, N+1):
		s.add(i)

	# Generate prefix minimum array
	for i in range(0, N):
		# Length remaining
		len = N - i
		val = findValue(len, Y)
		ans[i] = val
		Y -= val
		if (val in s):
			s.remove(val)

	# Remove duplicates to make array permutation
	# So, iterate in reverse order
	for i in range(N-1, -1, -1):
		if (ans[i] == ans[i - 1]):
			# Find minimum element not taken
			# in the permutation
			ans[i] = list(s)[0]
			s.remove(ans[i])

	# Print the permutation
	for i in ans:
		print(i, end=" ")

	print()

# Driver Code
if __name__ == "__main__":

	N, Y = 5, 10

	generatePermutation(N, Y)

# This code is contributed by rakeshsahni
