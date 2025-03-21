# Python3 program to find all
# pair in both arrays whose
# sum is equal to given value x

# Function to find all pairs
# in both arrays whose sum is
# equal to given value x
def findPairs(arr1, arr2, n, m, x):

	# Insert all elements of
	# first array in a hash
	s = set()
	for i in range (0, n):
		s.add(arr1[i])

	# Subtract sum from second
	# array elements one by one
	# and check it's present in
	# array first or not
	for j in range(0, m):
		if ((x - arr2[j]) in s):
			print((x - arr2[j]), '', arr2[j])

# Driver code
arr1 = [1, 0, -4, 7, 6, 4]
arr2 = [0, 2, 4, -3, 2, 1]
x = 8

n = len(arr1)
m = len(arr2)
findPairs(arr1, arr2, n, m, x) 
