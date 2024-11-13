# Python code to sum list of tuples having same first value

# Importing
from collections import defaultdict

# Initialisation of list of tuple
Input = [(2, 190), (1, 13), (1, 12),
		(2, 14), (3, 82), (1, 70)]

# Initialisation of defaultdict
output = defaultdict(int)

for k, v in Input:
	output[k] += v

# Printing output
print(list(output.items()))
