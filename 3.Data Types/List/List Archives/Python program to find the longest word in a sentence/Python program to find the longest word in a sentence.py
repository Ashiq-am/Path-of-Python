# Python3 program for the above approach

# Function to print the longest
# word in given sentence
def largestWord(s):

	# Sort the words in increasing
	# order of their lengths
	s = sorted(s, key = len)

	# Print last word
	print(s[-1])


# Driver Code
if __name__ == "__main__":

	# Given string
	s = "be confident and be yourself"

	# Split the string into words
	l = list(s.split(" "))

	largestWord(l)
