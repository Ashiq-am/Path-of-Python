# Python program to get transpose
# elements of two dimension list
def transpose(l1, l2):

	# star operator will first
	# unpack the values of 2D list
	# and then zip function will
	# pack them again in opposite manner
	l2 = list(map(list, zip(*l1)))
	return l2

# Driver code
l1 = [[4, 5, 3, 9], [7, 1, 8, 2], [5, 6, 4, 7]]
l2 = []
print(transpose(l1, l2))


