# python3 code to implement the above approach
from bisect import bisect_left

# Function to find the maximum number
# of elements that can be deleted
def solve(v, n):

	pref = [0 for _ in range(n)]
	suff = [0 for _ in range(n)]

	# Storing the same value of the array in
	# prefix and suffix array
	for i in range(0, n):
		pref[i] = suff[i] = v[i]

	# Calculating prefix sum
	for i in range(1, n):
		pref[i] = pref[i] + pref[i - 1]

	# Calculating suffix sum
	for i in range(n-2, -1, -1):
		suff[i] = suff[i] + suff[i + 1]

	# Initializing answer with 0
	ans = 0

	for i in range(n-1, 0, -1):

		# Finding the lower bound of the
		# element with suffix sum
		z = bisect_left(pref, suff[i], lo=0, hi=i - 1)

		# Calculating the index
		idx = z

		# If the value at index matches with
		# suffix sum we will calculate the
		# total number of elements
		if (pref[idx] == suff[i]):
			temp = 0
			temp = temp + (n - i)
			temp = temp + (idx + 1)

			# Updating the answer to store
			# the maximum
			ans = max(ans, temp)

	# Printing answer
	print(ans)

# Driver code
if __name__ == "__main__":

	arr = [70, 80, 85, 70, 80]
	N = len(arr)

	# Function call
	solve(arr, N)

	# This code is contributed by rakeshsahni
