# Python3 code to convert tuple
# into string
def convertTuple(tup):
	str = ''.join(tup)
	return str

# Driver code
tuple = ('g', 'e', 'e', 'k', 's')
str = convertTuple(tuple)
print(str)
