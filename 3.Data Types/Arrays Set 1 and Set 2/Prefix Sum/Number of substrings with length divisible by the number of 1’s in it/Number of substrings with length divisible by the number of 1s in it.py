# Python3 program to count number of
# substring under given condition

# Function return count of
# such substing
def countOfSubstrings(s):
	n = len(s)
	prefix_sum = [0 for i in range(n)]

	# Mark 1 at those indices
	# where '1' appears
	for i in range(n):
		if (s[i] == '1'):
			prefix_sum[i] = 1

	# Take prefix sum
	for i in range(1, n, 1):
		prefix_sum[i] += prefix_sum[i - 1]

	answer = 0

	# Iterate through all the
	# substrings
	for i in range(n):
		for j in range(i, n, 1):
			if (i - 1 >= 0):
				countOfOnes = prefix_sum[j]- prefix_sum[i - 1]
			else:
				countOfOnes = prefix_sum[j]
			length = j - i + 1

			if (countOfOnes > 0 and length % countOfOnes == 0):
				answer += 1

	return answer

# Driver Code
if __name__ == '__main__':
	S = "1111100000"

	print(countOfSubstrings(S))
