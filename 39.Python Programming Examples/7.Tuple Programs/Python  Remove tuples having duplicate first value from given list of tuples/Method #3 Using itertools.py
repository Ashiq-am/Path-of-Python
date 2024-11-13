# Python code to remove tuples having
# duplicate first value from given
# list of tuples

import itertools

# Input list initialization
Input = [(12.121, 'Geeksforgeeks is best'),
		(19212.22, 'India is best'),
		(923232.2323, 'Cyware is best.'),
		(923232.2323, 'Jiit is best')]

# Using groupby
Output = ([next(b) for a, b in itertools.groupby(
						Input, lambda y: y[0])])

# Printing
print("Initial list of tuple is\n", Input)
print("\nList of tuple after removing duplicates\n", Output)
