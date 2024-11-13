# Function to Sort even-placed elements
# in increasing and odd-placed in decreasing
# order

def evenOddSort(input):

	# separate even odd indexed elements list
	evens = [ input[i] for i in range(0,len(input)) if i%2==0 ]
	odds = [ input[i] for i in range(0,len(input)) if i%2!=0 ]

	# sort evens in ascending and odds in
	# descending using sorted() method
	print (sorted(evens) + sorted(odds,reverse=True))

# Driver program
if __name__ == "__main__":
	input = [0, 1, 2, 3, 4, 5, 6, 7]
	evenOddSort(input)
