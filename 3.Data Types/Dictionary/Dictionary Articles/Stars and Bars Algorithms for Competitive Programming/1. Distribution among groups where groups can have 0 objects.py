# Function to calculate C(N, R)
def C(N, R):
	R = min(R, N - R)
	ans = 1
	for i in range(R):
		ans = ans * (N - i)
		ans = ans // (i + 1)
	return ans

# Function to get ways where groups can have 0 objects
def getWaysWithZero(N, K):
	return C(N + K - 1, K - 1)


# Number of objects and groups
N, K = 4, 2
print("Ways to divide", N, "objects among", K,
	"groups such that a group can have 0 objects are",
	getWaysWithZero(N, K))
