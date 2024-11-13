# Python3 implementation of
# the above approach

# Function to print the list containing
# the sum of key and value pairs of
# each item of a dictionary
def FindSum(arr):

	# Stores the list containing the
	# sum of keys and values of each item
	l = []

	# Traverse the dictionary
	for i in arr:

		l.append(i + arr[i])

	# Print the list l
	print(*l)

# Driver Code

arr = {1: 10, 2: 20, 3: 30}

FindSum(arr)
