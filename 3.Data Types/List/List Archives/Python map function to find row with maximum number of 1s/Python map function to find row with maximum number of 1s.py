# Function to find the row with maximum number of 1's
def maxOnes(input):

	# map sum function on each row of
	# given matrix
	# it will return list of sum of all one's
	# in each row, then find index of maximum element
	result = list(map(sum,input))
	print (result.index(max(result)))

# Driver program
if __name__ == "__main__":
	input = [[0, 1, 1, 1],[0, 0, 1, 1],[1, 1, 1, 1],[0, 0, 0, 0]]
	maxOnes(input)
