import sys

sys.setrecursionlimit(10**6)

N = 5 * 10**3 + 15

# dp table for memoization
dp = [[-1, -1] for _ in range(N)]

n, x, y, z = 0, 0, 0, 0
A, B = "", ""

# vector to store indices which differ in string A and B
v = []


def solve(idx, flag):
	global dp, x, y, z, v

	if idx > z:
		return 1e10
	if idx == z:
		return 0
	if dp[idx][flag] != -1:
		return dp[idx][flag]

	cost = 0
	# If the current index is not the last index of A
	if idx + 1 < z:
		# We cannot change the current index free of cost
		if not flag:
			cost = min(solve(idx + 1, 1) + y,
					solve(idx + 2, 0) + (v[idx + 1] - v[idx]) * x)
		# We can change the current index free of cost
		else:
			cost = min(solve(idx + 1, 0),
					solve(idx + 2, 1) + (v[idx + 1] - v[idx]) * x)
	# If the current index is the last index of A
	else:
		# We have to change the current index with some
		# previous operation
		cost = solve(idx + 1, 0)

	dp[idx][flag] = cost
	return cost


def main():
	global A, B, x, y, n, v, z, dp

	A = "10000011000001"
	B = "00000000000000"
	x = 8
	y = 9
	n = len(A)
	for i in range(n):
		if A[i] != B[i]:
			v.append(i)
	z = len(v)

	# If the number of different indices is odd, then it is
	# impossible to convert A to B
	if z % 2:
		print(-1)
	else:
		for i in range(z + 1):
			dp[i][1] = dp[i][0] = -1
		print(solve(0, 0))


if __name__ == "__main__":
	main()
