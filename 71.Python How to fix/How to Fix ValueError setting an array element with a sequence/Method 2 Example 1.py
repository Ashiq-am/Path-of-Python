# In this program we are demostraiting how mismatch
# of data-type can cause value error

import numpy

# Creating array
array1 = ["Geeks", "For"]

# Default Data type of Array
Data_type = str


np_array = numpy.array(array1, dtype=Data_type)
# This cause error
np_array[1] = ["for", "Geeks"]
print(np_array)
