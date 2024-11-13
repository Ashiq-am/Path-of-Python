# Python3 implementation of the given approach.

# Tail recursive function
def arrSum(array, size, Sum = 0):

	# Base Case
	if size == 0:
		return Sum

	# Function Call Observe sum+array[size-1]
	# to maintain sum of elements
	return arrSum(array, size - 1,
			Sum + array[size - 1])

# Driver Code
if __name__ == "__main__":

	array = [2, 55, 1, 7]
	size = len(array)
	print(arrSum(array, size)) 
