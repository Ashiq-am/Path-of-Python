# Python3 implementation of the approach

# Function to return the maximum number
# of given operations required to
# remove the given entirely
def find(s):

	# If length of the is zero
	if (len(s) == 0):
		return 0

	# Single operation can delete
	# the entire string
	c = 1

	# To store the prefix of the string
	# which is to be deleted
	d = ""

	for i in range(len(s)):

		# Prefix s[0..i]
		d += s[i]

		# To store the subs[i+1...2*i+1]
		s2 = s[i + 1:i + 1 + len(d)]

		# If the prefix s[0...i] can be deleted
		if (s2 == d):

			# 1 operation to remove the current prefix
			# and then recursively find the count of
			# operations for the subs[i+1...n-1]
			c = 1 + find(s[i + 1:])
			break

	# Entire has to be deleted
	return c

# Driver code
s = "abababab"
print(find(s))

# This code is contributed by Mohit Kumar
