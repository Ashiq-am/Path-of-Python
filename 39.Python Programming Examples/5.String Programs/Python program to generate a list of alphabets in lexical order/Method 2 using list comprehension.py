def generateAlphabetListDynamically(size=26):
	size = 26 if (size > 26 or size <= 0) else size

	# Here we are looping from 0 to upto specified size
	# 65 is added because it is ascii equivalent of 'A'
	alphabetList = [chr(i+65) for i in range(size)]

	# returning the list
	return alphabetList


# Calling the function to get the alphabets
alphabetList = generateAlphabetListDynamically()
print('The alphabets in the list are:', *alphabetList)
