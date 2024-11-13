# Python code to implement the approach

# Function to find the minimum cost
def minCost(s):
	n = len(s)
	count0 = 0
	ans = float('inf')
	for i in range(n):
		if(s[i] == '0'):
			count0 += 1

	prefixCountZero = [0]*n
	suffixCountZero = [0]*n

	# Loop to find the prefix count of 0
	for i in range(n):
		if(i != 0):
			prefixCountZero[i] = prefixCountZero[i-1]
		if(s[i] == '0'):
			prefixCountZero[i] += 1

	# Loop to find the suffix count of 0
	for i in range(n-1, -1, -1):
		if(i != n-1):
			suffixCountZero[i] = suffixCountZero[i+1]
		if(s[i] == '0'):
			suffixCountZero[i] += 1

	# Loop to find the minimum cost
	for i in range(count0+1):
		if(i == 0):
			x = count0 - suffixCountZero[n - count0]
		elif(i == count0):
			x = count0 - prefixCountZero[count0 - 1]
		else:
			x = count0 - prefixCountZero[i-1] - suffixCountZero[n-(count0 - i)]
		ans = min(ans, x)

	return ans

S = "101110110"

# Function call
print(minCost(S))

# This code is contributed by lokeshmvs21.
