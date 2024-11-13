# Importing required modules
import numpy

# Initializing the list
List = ["Geeks", 4, 'Geeks!']

# Converting to array
Array = numpy.array(List)

# Using enumerate
for ele in numpy.nditer(Array):
	print(ele, end=" ")
