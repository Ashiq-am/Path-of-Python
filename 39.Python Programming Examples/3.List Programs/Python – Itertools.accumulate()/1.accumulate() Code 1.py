# import the itertool module
# to work with it
import itertools

# import operator to work
# with operator
import operator

# creating a list GFG
GFG = [1, 2, 3, 4, 5]

# using the itertools.accumulate()
result = itertools.accumulate(GFG,
							operator.mul)

# printing each item from list
for each in result:
	print(each)
