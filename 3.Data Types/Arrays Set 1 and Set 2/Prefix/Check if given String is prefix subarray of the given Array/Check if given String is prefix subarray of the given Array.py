# Pyhton program to implement the
# given approach

# Function to check whether string
# is prefix
def isPrefixString(s, word):

	# ans is taken as an empty string
	ans = ""

	# N is used to store
	# the size of word array
	N = len(word)

	# Iterating over the word array
	for i in range(0, N):

		# Adding element by element
		# of the array
		ans = ans + (word[i])

		# If ans and str are same
		# return true
		if (ans == s):
			return True

	# As iteration is ending which means
	# string is not prefix so return false.
	return False

# Driver code
str = "indiaismycountry"
word = ["india", "is", "my", "country", "and", "i", "love", "india"]

ans = isPrefixString(str, word)
if (ans == True):
	print("True")
else:
	print("False")

# This code is contributed by Samim Hossain Mondal.
