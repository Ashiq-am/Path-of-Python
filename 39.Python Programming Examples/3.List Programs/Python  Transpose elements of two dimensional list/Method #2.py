# Python program to get transpose
# elements of two dimension list
def transpose(l1, l2):

	# we have nested loops in comprehensions
	# value of i is assigned using inner loop
	# then value of item is directed by row[i]
	# and appended to l2
	l2 =[[row[i] for row in l1] for i in range(len(l1[0]))]
	return l2

# Driver code
l1 = [[4, 5, 3, 9], [7, 1, 8, 2], [5, 6, 4, 7]]
l2 = []
print(transpose(l1, l2))
