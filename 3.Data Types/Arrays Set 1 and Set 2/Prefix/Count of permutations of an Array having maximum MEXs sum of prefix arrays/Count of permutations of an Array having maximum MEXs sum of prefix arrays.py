# Python Program to implement
# the above approach

# To calculate the factorial
def factorial(n):
	res = 1
	for i in range(2, n + 1):
		res *= i
	return res

# To return the number of permutations of
# an array with maximum MEXs sum of prefix array
def countPermutations(ar, n):

	# Map to store the frequency of each element
	mp = dict()

	ans = 1
	cnt = n

	for i in range(n):

		if (ar[i] in mp):
			mp[ar[i]] += 1
		else:
			mp[ar[i]] = 1

	# Running a loop from i=0 to i<n
	for i in range(n):

		# If continuity breaks,
		# then break the loop
		if (i not in mp):
			break

		# Considering choices available to be
		# filled at this position, i.e. mp[i]
		ans = (ans * mp[i])

		# Decrement the count of remaining
		# right elements
		cnt -= 1

	# Adding all permutations of the
	# elements present to the right of
	# the point where continuity breaks.
	ans = ans * factorial(cnt)

	return ans

# Driver Code
arr = [1, 0, 1]
N = len(arr)
print(countPermutations(arr, N))

# This code is contributed by gfgking
