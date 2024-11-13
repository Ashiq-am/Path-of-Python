# Python3 code to demonstrate
# Row with Maximum Product
# using max() + key

# getting Product
def prod(val) :
	res = 1
	for ele in val:
		res *= ele
	return res

# initializing matrix
test_matrix = [[1, 3, 1], [4, 5, 3], [1, 2, 4]]

# printing the original matrix
print ("The original matrix is : " + str(test_matrix))

# using max() + key
# Row with Maximum Product
res = max(test_matrix, key = prod)

# printing result
print ("Maximum product row is : " + str(res))
