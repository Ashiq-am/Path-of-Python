# Python Code
def MaxBalancedSubsequenceScore(n, stockPrice):
	# Create a dictionary to store
	# the difference and cumulative stock prices
	mp = {}
	maxm = 0
	for i in range(n):
		# Calculate the difference
		# between stock price and index
		diff = stockPrice[i] - i

		# Add the stock price to
		# the corresponding difference
		if diff in mp:
			mp += stockPrice[i]
		else:
			mp = stockPrice[i]

	# Find the maximum score
	# by iterating through the dictionary
	for key, value in mp.items():
		if value > maxm:
			# Update the maximum score
			# if a higher score is found
			maxm = value

	# Return the maximum score
	return maxm


# Driver code
stockPrice1 = [1, 5, 3, 7, 8]
# Function Call
print(MaxBalancedSubsequenceScore(len(stockPrice1), stockPrice1))
stockPrice2 = [1, 2, 3]
# Function Call
print(MaxBalancedSubsequenceScore(len(stockPrice2), stockPrice2))
