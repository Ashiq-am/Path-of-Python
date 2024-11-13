# Python3 program for the above approach

# Function to print all the words
# occurring k times in a string


def kFreqWords(S, K):

	# Stores the words
	l = list(S.split(" "))

	# Traverse the list
	for i in l:

		# Check for count
		if l.count(i) == K:

			# Print the word
			print(i)

			# Remove from list
			l.remove(i)


# Driver Code
if __name__ == "__main__":

	# Given string
	S = "banana is in yellow and sun flower is also in yellow"

	# Given value of K
	K = 2

	# Function call to find
	# all words occuring K times
	kFreqWords(S, K)
