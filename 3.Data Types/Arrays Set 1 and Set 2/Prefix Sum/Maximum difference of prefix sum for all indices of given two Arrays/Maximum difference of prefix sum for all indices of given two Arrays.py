# python3 program for the above approach

# Function to get the winner


def getWinner(a, s, N):

	maxDiff = abs(a[0] - s[0])

	# Calculating prefix sum
	for i in range(1, N):
		a[i] += a[i - 1]
		s[i] += s[i - 1]
		maxDiff = max(maxDiff, abs(a[i] - s[i]))

	# Return the result
	return maxDiff


# Driver Code
if __name__ == "__main__":

	N = 5

	a = [20, 20, 35, 20, 35]
	s = [21, 31, 34, 41, 14]

	print(getWinner(a, s, N))

# This code is contributed by rakeshsahni
