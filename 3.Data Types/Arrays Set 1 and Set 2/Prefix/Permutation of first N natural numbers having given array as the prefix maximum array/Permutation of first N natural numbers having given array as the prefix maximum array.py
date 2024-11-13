# Python3 program for the above approach
import sys

# Function to check if the maximum
# prefix array of ans[] is equal
# to array arr[]
def checkPermutation(ans, a, n):

	# Initialize a variable, Max
	Max = -sys.maxsize - 1

	# Traverse the array, ans[]
	for i in range(n):

		# Store the maximum value
		# upto index i
		Max = max(Max, ans[i])

		# If it is not equal to a[i],
		# then return false
		if (Max != a[i]):
			return False

	# Otherwise return false
	return True

# Function to find the permutation of
# the array whose prefix maximum array
# is same as the given array a[]
def findPermutation(a, n):

	# Stores the required permutation
	ans = [0] * n

	# Stores the index of first
	# occurrence of elements
	um = {}

	# Traverse the array a[]
	for i in range(n):

		# If a[i] is not present
		# in um, then store it in um
		if (a[i] not in um):

			# Update the ans[i]
			# to a[i]
			ans[i] = a[i]
			um[a[i]] = i

	# Stores the unvisited numbers
	v = []
	j = 0

	# Fill the array, v[]
	for i in range(1, n + 1):

		# Store the index
		if (i not in um):
			v.append(i)

	# Traverse the array, ans[]
	for i in range(n):

		# Fill v[j] at places where
		# ans[i] is 0
		if (ans[i] == 0):
			ans[i] = v[j]
			j += 1

	# Check if the current permutation
	# maximum prefix array is same as
	# the given array a[]
	if (checkPermutation(ans, a, n)):

		# If true, the print the
		# permutation
		for i in range(n):
			print(ans[i], end = " ")

	# Otherwise, print -1
	else:
		print("-1")

# Driver Code
if __name__ == "__main__":

	arr = [ 1, 3, 4, 5, 5 ]
	N = len(arr)

	# Function Call
	findPermutation(arr, N)

# This code is contributed by ukasp
