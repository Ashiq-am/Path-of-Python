# Python code to remove all characters
# other than alphabets from string

def removeAll(input):

	# Traverse complete string and separate
	# all characters which lies between [a-z] or [A-Z]
	sepChars = [char for char in input if
ord(char) in range(ord('a'),ord('z')+1,1) or ord(char) in
range(ord('A'),ord('Z')+1,1)]

	# join all separated characters
	# and print them together
	return ''.join(sepChars)

# Driver program
if __name__ == "__main__":
	input = "$Gee*k;s..fo, r'Ge^eks?"
	print (removeAll(input))
