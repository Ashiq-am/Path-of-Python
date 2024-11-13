# Function to find duplicate rows in a binary matrix
from collections import Counter

def duplicate(input):

	# since lists are unhasable for counter method
	# because lists are mutable so first we will cast
	# each row (list) into tuple
	input = map(tuple,input)

	# now create dictionary
	freqDict = Counter(input)

	# print all rows having frequency greater than 1
	for (row,freq) in freqDict.items():
		if freq>1:
			print (row)

# Driver program
if __name__ == "__main__":
	input = [[1, 1, 0, 1, 0, 1],
			[0, 0, 1, 0, 0, 1],
			[1, 0, 1, 1, 0, 0],
			[1, 1, 0, 1, 0, 1],
			[0, 0, 1, 0, 0, 1],
			[0, 0, 1, 0, 0, 1]]
	duplicate(input)
