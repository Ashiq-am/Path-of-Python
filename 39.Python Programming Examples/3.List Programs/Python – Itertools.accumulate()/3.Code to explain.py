# import the itertool module to
# work with it
import itertools


# creating a set GFG1 and GFG2
GFG1 = { 5, 3, 6, 2, 1, 9 }
GFG2 ={ 4, 2, 6, 0, 7 }

# using the itertools.accumulate()

# Now this will first give difference
# and the give result by adding all
# the element in result as by default
# if no function passed it will add always
result = itertools.accumulate(GFG2.difference(GFG1))

# printing each item from list
for each in result:
	print(each)
