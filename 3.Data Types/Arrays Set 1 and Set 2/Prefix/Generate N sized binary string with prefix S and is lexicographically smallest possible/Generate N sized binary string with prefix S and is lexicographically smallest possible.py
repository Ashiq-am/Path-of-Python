# Python program for above approach

# Function to build string
def find_string(n, s):

	# Declaring variable
	count0 = 0
	count1 = 0

	# Check number of 1's and 0's
	for i in range(len(s)):
		if (s[i] == '0'):
			count0 += 1
		else:
			count1 += 1
	sb = s

	# Store difference in number of 1's
	# and 0's
	g = count0 - count1

	# l store the value that how much 0's
	# or 1's we need to add in string
	l = n - len(s)
	l -= g

	# u store the count of
	# number of 0's we need to insert
	u = l // 2
	while (u > 0):
		sb += '0'
		u -= 1
	if (l % 2 != 0):
		sb += '0'

	while (len(sb) < n):
		sb += '1'

	# Return result
	return sb

# Driver Code
N = 7
S = "001"

# Function call
print(find_string(N, S))

# This code is contributed by shinjanpatra
