# Python3 program for the above approach

from itertools import chain

# Function to print all unique keys
# from a list of dictionaries
def UniqueKeys(arr):

	# Stores the list of unique keys
	res = list(set(val for dic in arr for val in dic.keys()))

	# Print the list
	print(str(res))

# Driver Code

# Input
arr = [{'my': 1, 'name': 2},
	{'is': 1, 'my': 3},
	{'ria': 2}]

UniqueKeys(arr)
