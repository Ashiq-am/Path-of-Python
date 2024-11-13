# Python3 code to convert tuple
# into string
import functools
import operator

def convertTuple(tup):
	str = functools.reduce(operator.add, (tup))
	return str

# Driver code
tuple = ('g', 'e', 'e', 'k', 's')
str = convertTuple(tuple)
print(str)
