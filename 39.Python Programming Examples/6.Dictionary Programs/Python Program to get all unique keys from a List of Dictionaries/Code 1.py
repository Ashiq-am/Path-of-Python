# Python3 program for the above approach
from itertools import chain


# Function to print all unique keys
# present in a list of dictionaries
def UniqueKeys(arr):

	# Stores the list of unique keys
	res = list(set(chain.from_iterable(sub.keys() for sub in arr)))

	# Print the list
	print(str(res))

# Driver Code
arr = [{'my': 1, 'name': 2},
	{'is': 1, 'my': 3},
	{'ria': 2}]
UniqueKeys(arr)
