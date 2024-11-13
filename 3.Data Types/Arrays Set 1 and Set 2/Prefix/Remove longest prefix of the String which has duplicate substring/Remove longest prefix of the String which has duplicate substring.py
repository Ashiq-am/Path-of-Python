# Python code for the above approach:

# Function to delete the longest prefix
def delPrefix(S):

	if (len(S) == 1):
		return S
	i = 0
	maxi = 0

	# Loop to find the
	# longest duplicate of prefix
	for j in (1, len(S)+1):
		k = j
		while (k < len(S) and S[k] == S[i]):
			k = k + 1
			i = i + 1

		maxi = max(maxi, i)
		i = 0

	return S[maxi:]

# Driver code
S = "aaaaa"
ans = delPrefix(S)

# Function call
print(ans)

# This code is contributed by Taranpreet
