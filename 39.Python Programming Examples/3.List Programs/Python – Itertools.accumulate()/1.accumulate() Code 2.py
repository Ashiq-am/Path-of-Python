# import the itertool module
# to work with it
import itertools

# import operator to work with
# operator
import operator

# creating a list GFG
GFG = [5, 3, 6, 2, 1, 9, 1]

# using the itertools.accumulate()

# Now here no need to import operator
# as we are not using any operator
# Try after removing it gives same result
result = itertools.accumulate(GFG, max)

# printing each item from list
for each in result:
	print(each)
