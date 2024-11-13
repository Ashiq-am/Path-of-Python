# Python code for the above approach

# Function to find all the indices
def findIndices (arr, K, N):
	prefix = [0] * N
	suffix = [0] * N
	ans = [];

	prefix[0] = 0;
	for i in range(1, N):
		if (arr[i] <= arr[i - 1]):
			prefix[i] = prefix[i - 1] + 1;
		else:
			prefix[i] = 0;


	suffix[N - 1] = 0;
	for i in range(N - 2, 1, -1):
		if (arr[i] <= arr[i + 1]):
			suffix[i] = suffix[i + 1] + 1;
		else:
			suffix[i] = 0;


	for i in range(N):
		if (prefix[i] >= K and suffix[i] >= K):
			ans.append(i);

	return ans;

# Driver code
arr = [1, 1, 1, 1, 1];
K = 0;
N = len(arr)
ans = findIndices(arr, K, N);
for i in range(len(ans)):
	print(ans[i], end=" ");
if (len(ans) == 0):
	print("-1");

# This code is contributed by Saurabh Jaiswal
