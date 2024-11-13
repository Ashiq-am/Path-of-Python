# Python3 implementation of the above approach

# Function that finds minimum number
# of colors required
def colorRequired(arr, n):

	# To check that if all the elements
	# are same or not
	all_same = True

	# To check if only one adjacent exist
	one_adjacent_same = False

	# Traverse the array
	for i in range(n - 1):

		# If adjacent elements found
		# different means all are not
		# same
		if(arr[i] != arr[i + 1]):
			all_same = False

		# If two adjacent elements
		# found to be same then make
		# one_adjacent_same true
		if(arr[i] == arr[i + 1]):
			one_adjacent_same = True

	# If all elements are same
	# then print 1
	if(all_same == True):
		print(1)
		return

	# If total number of elements are
	# even or there exist two adjacent
	# elements that are same
	# then print 2
	if(n % 2 == 0 or one_adjacent_same == True):
		print(2)
		return

	# Else 3 type of colors
	# are required
	print(3)

# Driver Code
if __name__ == '__main__':

	arr = [ 1, 2, 1, 1, 2 ]
	n = len(arr)

	# Function call
	colorRequired(arr, n)


