# Python program to count number of items
# in a dictionary value that is a list.
def main():

	# defining the dictionary
	d = {'A' : [1, 2, 3, 4, 5, 6, 7, 8, 9],
		'B' : 34,
		'C' : 12,
		'D' : [7, 8, 9, 6, 4] }

	# using the in operator
	count = 0
	for x in d:
		if isinstance(d[x], list):
			count += len(d[x])
	print(count)

# Calling Main
if __name__ == '__main__':
	main()
