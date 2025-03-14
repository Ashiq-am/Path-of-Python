# function to Reverse an array in groups of given size

def reverseGroup(input,k):

	# set starting index at 0
	start = 0

	# run a while loop len(input)/k times
	# because there will be len(input)/k number
	# of groups of size k
	result = []
	while (start<len(input)):

		# if length of group is less than k
		# that means we are left with only last
		# group reverse remaining elements
		if len(input[start:])<k:
				result = result + list(reversed(input[start:]))
				break

		# select current group of size of k
		# reverse it and concatenate
		result = result + list(reversed(input[start:start + k]))
		start = start + k
	print(result)

# Driver program
if __name__ == "__main__":
	input = [1, 2, 3, 4, 5, 6, 7, 8]
	k = 5
	reverseGroup(input,k)
