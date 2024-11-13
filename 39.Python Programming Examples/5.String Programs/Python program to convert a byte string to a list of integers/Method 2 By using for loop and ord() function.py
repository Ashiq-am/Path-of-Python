# Python program to illustrate the
# conversion of a byte string
# to a list of integers

# Initializing a byte string
S = "GFG is a CS Portal"

nums = []

# Calling the for loop to iterate each
# characters of the given byte string
for chr in S:

	# Calling the ord() function
	# to convert the specified byte
	# characters to numbers of the unicode
	nums.append(ord(chr))

# Printing the unicode of the byte string
print(nums)
