# Python code to remove tuples having
# duplicate first value from given
# list of tuples

from collections import OrderedDict

# Input list initialization
Input = [(12.121, 'Geeksforgeeks is best'),
		(19212.22, 'India is best'),
		(19212.22, 'Cyware is best.'),
		(923232.2323, 'Jiit is best')]

# Using orderedDIct
Output = OrderedDict(Input).items()

# Printing
print("Initial list of tuple is\n", Input)
print("\nList of tuple after removing duplicates\n", Output)
