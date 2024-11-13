# Python program to count number of items
# in a dictionary value that is a list.
def main():

	# defining the dictionary
	d = {'A' : [1, 2, 3, 4, 5, 6, 7, 8, 9],
		'B' : 34,
		'C' : 12,
		'D' : [7, 8, 9, 6, 4] }

	# using enumerate()
	count = 0
	for x in enumerate(d.items()):

		# enumerate function returns a tuple in the form
		# (index, (key, value)) it is a nested tuple
		# for accessing the value we do indexing x[1][1]
		if isinstance(x[1][1], list):
			count += len(x[1][1])
	print(count)

if __name__ == '__main__':
	main()
