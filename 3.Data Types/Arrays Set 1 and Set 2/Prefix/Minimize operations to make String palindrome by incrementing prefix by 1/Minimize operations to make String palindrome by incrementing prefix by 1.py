# Python code to implement the approach
import math

# Function to find minimum operation
# to convert string into palindrome
def minOperation(str, n):

	j = n - 1
	i = 0
	maxi = 99999999
	ans = 0
	while (j > i):
		if (str[j] < str[i]):
			return -1

		k =abs(ord(str[j]) - ord(str[i]))
		ans = max(ans, k)
		if (maxi < k):
			return -1

		maxi = k
		i = i + 1
		j = j - 1

	return ans

# Driver Code
S = "1234"
N = len(S)
print(minOperation(S, N))

# This code is contributed by Potta Lokesh.
