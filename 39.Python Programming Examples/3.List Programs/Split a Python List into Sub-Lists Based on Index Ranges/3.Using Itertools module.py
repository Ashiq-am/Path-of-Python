from itertools import islice

# Input list initialization
Input = [11, 2, 13, 4, 15, 6, 7]

# list of length in which we have to split
Index_range = [[1, 4], [3, 6]]

# Using islice
Output = [list(islice(Input, elem[0], elem[1]+1))
		for elem in Index_range]
print(Output)
