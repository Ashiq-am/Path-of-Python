# Function to find sums of ASCII values of each
# word in a sentence in

def asciiSums(sentence):

	# split words separated by space
	words = sentence.split(' ')

	# create empty dictionary
	result = {}

	# calculate sum of ascii values of each word
	for word in words:
		currentSum = sum(map(ord,word))

		# map sum and word into resultant dictionary
		result[word] = currentSum

	totalSum = 0

	# iterate list of splited words in order to print
	# sum of ascii values of each word sequentially
	sumsOfAscii = [result[word] for word in words]
	print ('Sum of ASCII values:')
	print (' '.join(map(str,sumsOfAscii)))
	print ('Total Sum -> ',sum(sumsOfAscii))

# Driver program
if __name__ == "__main__":
	sentence = 'I am a geek'
	asciiSums(sentence)
