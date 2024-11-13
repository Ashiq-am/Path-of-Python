# open a file
file = open("test.txt")

# lines to print
specified_lines = [0, 7, 11]

# loop over lines in a file
for pos, l_num in enumerate(file):
	# check if the line number is specified in the lines to read array
	if pos in specified_lines:
		# print the required line number
		print(l_num)
