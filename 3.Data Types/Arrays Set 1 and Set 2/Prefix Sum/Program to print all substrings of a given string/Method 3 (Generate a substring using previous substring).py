'''
* Python3 program to prall possible
* substrings of a given string
* without checking for duplication.
'''


'''
* Function to prall (n * (n + 1)) / 2
* substrings of a given string s of length n.
'''
def printAllSubstrings(s, n):

	# Fix start index in outer loop.
	# Reveal new character in inner loop till end of string.
	# Prtill-now-formed string.
	for i in range(n):
		temp=""
		for j in range(i,n):
			temp+=s[j]
			print(temp)

# Driver program to test above function

s = "Geeky"
printAllSubstrings(s, len(s))

