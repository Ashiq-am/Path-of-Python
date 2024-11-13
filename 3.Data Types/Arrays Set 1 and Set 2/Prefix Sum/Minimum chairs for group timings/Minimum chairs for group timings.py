# Python code for the above approach:
def minChairsToSeat(N, T1, T2, S):
	# Create a range
	range_ = [0] * (10**6)
	maxVal = 0

	# Store the range in the given list
	for i in range(N):
		range_[T1[i]] += S[i]
		range_[T2[i] + 1] -= S[i]

	for i in range(1, 10**5 + 1):
		range_[i] += range_[i - 1]
		maxVal = max(maxVal, range_[i])

	return maxVal

# Driver's code
if __name__ == '__main__':
	N = 5
	T1 = [7, 18, 16, 14, 16]
	T2 = [18, 21, 23, 16, 22]
	S = [8, 11, 20, 4, 7]

	# Function call
	print(minChairsToSeat(N, T1, T2, S))
