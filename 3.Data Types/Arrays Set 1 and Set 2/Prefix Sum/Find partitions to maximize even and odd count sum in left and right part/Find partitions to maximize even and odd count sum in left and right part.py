# python3 code to implement the approach

# Function to find the answer vector
def solve(vect):

	# To keep the track
	# of final answer
	maximumSum = 0

	# Size of nums
	n = len(vect)

	# It keeps the track
	# of final answer
	ans = []

	# Iterate over the indices
	for i in range(1, n):

		# Stores the count of even
		# numbers in the left subarray
		countEven = 0

		# Iterate in the left subarray
		for j in range(i-1, -1, -1):
			if (vect[j] % 2 == 0):
				countEven += 1

		# Stores the count of even
		# numbers in the left subarray
		countOdd = 0

		# Iterate in the right subarray
		for j in range(i, n):
			if (vect[j] % 2 == 1):
				countOdd += 1

		# Stores the sum for current i
		sum = countEven + countOdd

		# If current score
		# is greater than
		# previous then push
		# in the ans array.
		if (sum > maximumSum):
			ans = [i]
			maximumSum = sum

		# If sum is equal to
		# maximum sum then
		# consider the index i
		# with previous max
		elif (sum == maximumSum):
			ans.append(i)

	return ans

# Function to print answer
def pnt(ans):

	n = len(ans)
	for i in range(0, n):
		print(ans[i], end=' ')

# Driver code
if __name__ == "__main__":

	# Given vector
	vect = [1, 2, 3, 4, 5, 6, 7]

	# Function call
	ans = solve(vect)
	pnt(ans)
