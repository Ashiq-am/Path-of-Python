# Python3 code to implement the above approach

# Function to remove minimum number
# of brackets to make the string beautiful
def findMinRemoval(s):

	n = len(s)

	# Stores count of 0 from left to right
	left = [0] * n

	# Stores count of 1 from right to left
	right = [0] * n

	if (s[0] == '0'):
		left[0] = 1
	else:
		left[0] = 0

	# Calculate the prefix count of '0'
	# at every index
	for i in range(1, n):
		if (s[i] == '0'):
			left[i] = left[i - 1] + 1
		else:
			left[i] = left[i - 1]

	if (s[n - 1] == '1'):
		right[n - 1] = 1
	else:
		right[n - 1] = 0

	# Calculate the suffix count of '1'
	# at every index
	for i in range(n-2, -1, -1):
		if (s[i] == '1'):
			right[i] = right[i + 1] + 1
		else:
			right[i] = right[i + 1]

	Max = 0

	# Check for max length beautiful string
	for i in range(1,n):
		if (left[i - 1] == right[i]):
			Max = max(Max, 2 * right[i])
	return n - Max;

# Driver Code
if __name__ == "__main__":

	S = "01001101"

	# Function call
	print(findMinRemoval(S))
