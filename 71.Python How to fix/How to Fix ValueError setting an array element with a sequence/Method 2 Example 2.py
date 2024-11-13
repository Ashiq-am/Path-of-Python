# In this program we fix error by mismatch
# of data-type

import numpy

# Creating array
array1 = ["Geeks", "For"]

# Default Data type of Array
Data_type = str


np_array = numpy.array(array1, dtype=Data_type)

Variable = ["for", "Geeks"]

# First we match the data-type
if np_array.dtype == type(Variable):
	np_array[1] = Variable
else:
	print("Variable value is not the type of numpy array")
print(np_array)
