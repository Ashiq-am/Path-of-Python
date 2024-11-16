# Function to replace all occurrences of AB with C

def replaceABwithC(input, pattern, replaceWith):
	return input.replace(pattern, replaceWith)

# Driver program
if __name__ == "__main__":
	input = 'helloABworld'
	pattern = 'AB'
	replaceWith = 'C'
	print (replaceABwithC(input,pattern,replaceWith))
