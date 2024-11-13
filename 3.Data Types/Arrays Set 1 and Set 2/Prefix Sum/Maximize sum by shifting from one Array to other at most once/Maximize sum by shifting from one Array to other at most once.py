# Python code to implement the approach
# Function for calculating maximum sum
def maximiseSum(n, X, Y):

	# Suffix sum array of Y[]
	suf = [0]*n
	suf[n - 1] = Y[n - 1]

	# Variable to store sum of Y[]
	# ans the maximum possible sum
	sum = 0
	ans = 0

	# Loop for calculating suffix array of Y[]
	for i in range(n-2, -1, -1):
		sum += Y[i]
		suf[i] += suf[i + 1]
	ans = sum
	sum = 0

	# Loop to find out the maximum possible sum
	for i in range(n-1):
		sum += X[i]
		ans = max(ans, sum + suf[i + 1])
	sum += X[n - 1]
	ans = max(ans, sum)

	# Return the answer
	return ans

N = 4
X = [7, 5, 3, 4]
Y = [2, 3, 1, 3]
print(maximiseSum(N, X, Y))

# This code is contributed by vikkycirus.
