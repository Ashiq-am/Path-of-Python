# Python code to convert list of tuples into
# list of all digits which exists
# in elements of list.

# Importing
from itertools import chain

# Input list initialization
lst = [(11, 100), (22, 200), (33, 300), (44, 400), (88, 800)]

# using lambda
temp = map(lambda x: str(x), chain.from_iterable(lst))

# Output list initialization
Output = set()

# Adding element in Output
for x in temp:
	for elem in x:
		Output.add(elem)

# Printing output
print("Initial List is :", lst)
print("Output list is :", Output)
