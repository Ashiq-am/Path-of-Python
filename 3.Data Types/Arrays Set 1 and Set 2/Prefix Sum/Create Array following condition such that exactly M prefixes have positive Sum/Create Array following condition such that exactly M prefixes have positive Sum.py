# Python code to implement the approach


def solve(l, m):

	# Counter variable of integer DataType
	count = 0

	# String "ans" to hold arrangement
	ans = ""

	# Loop for applying discussed algorithm
	for i in range(1, l + 1):
		if (m <= l // 2):
			if (i % 2 == 1 and count < m):
				ans += str(i) + " "
				count += 1
			else:
				ans += str(-1 * i) + " "
		else:
			if (i % 2 == 1 and count < l - m):
				ans += str(-1 * i) + " "
				count += 1
			else:
				ans += str(i) + " "

	return ans


# Driver code
if __name__ == '__main__':

	# Input value of L and M
	N = 4
	M = 2

	print(solve(N, M))

# This code is contributed by Tapesh(tapeshdua420)
