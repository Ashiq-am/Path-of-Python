# Python3 program to find the
# number of occurrences of
# a character at position P upto p-1

# Function to find the number of occurrences
# of a character at position P upto p-1
def Occurrence(s, position):
	count = 0
	for i in range(position - 1):
		if (s[i] == s[position - 1]):
			count += 1

	# Return the required count
	return count

# Driver code
s = "ababababab"

p = 9

# Function call
print(Occurrence(s, p))

# This code is contributed by Mohit Kumar
