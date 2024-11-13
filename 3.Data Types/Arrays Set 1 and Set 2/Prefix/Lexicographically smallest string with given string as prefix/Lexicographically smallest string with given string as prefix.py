# Python 3 program for the above approach

# Function to find the whether the
# string temp starts with str or not
def is_prefix(temp, str):

	# Base Case
	if (len(temp) < len(str)):
		return 0
	else:

		# Check for the corresponding
		# characters in temp & str
		for i in range(len(str)):
			if (str[i] != temp[i]):
				return 0
		return 1

# Function to find lexicographic smallest
# string consisting of the string str
# as prefix
def lexicographicallyString(input, n, str):

	# Sort the given array string arr[]
	input.sort()

	for i in range(n):
		temp = input[i]

		# If the i-th string contains
		# given string as a prefix,
		# then print the result
		if (is_prefix(temp, str)):
			return temp

	# If no string exists then
	# return "-1"
	return "-1"

# Driver Code
if __name__ == '__main__':
	arr = ["apple", "appe", "apl", "aapl", "appax"]
	S = "app"
	N = 5

	print(lexicographicallyString(arr, N, S))

	# This code is contributed by ipg2016107.
