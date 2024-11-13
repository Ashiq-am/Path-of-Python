# Python code to implement above approach

# Function to calculate maximum points
# that can be collected
def maxTotalPoints(arr, M, K):
	MX = (int)(2e5 + 2);
	i, l, r, ans = 0, 0, 0, 0;

	# Incremented positions by one
	# to make calculations easier.
	M += 1;
	prefix_sum = [0 for i in range(MX)];
	for it in arr:
		prefix_sum[it[0] + 1] = it[1];
	for i in range(MX):
		prefix_sum[i] += prefix_sum[i - 1];

	for r in range(M, (M + K + 1) and ( r < MX and r <= M + K)):
		l = min(M, M - (K - 2 * (r - M)));
		l = max(1, l);
		ans = max(ans, prefix_sum[r] - prefix_sum[l - 1]);

	for l in range(M, (M - K - 1) and l > 0, -1):
		r = max(M, M + (K - 2 * (M - l)));
		r = min(MX - 1, r);
		ans = max(ans, prefix_sum[r] - prefix_sum[l - 1]);

	return ans;

# Driver code
if __name__ == '__main__':
	arr = [[2, 8], [6, 3], [8, 6]];
	M = 5;
	K = 4;
	print(maxTotalPoints(arr, M, K));

	# This code is contributed by 29AjayKumar
