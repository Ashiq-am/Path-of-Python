# In this program we fix problem by differnt data-type

import numpy

# Creating multi-dimension array
array1 = [1, 2, 4, [5, [6, 7]]]

# Object Data type is accept all data-type
Data_type = object

# Now we fix the error
np_array = numpy.array(array1, dtype=Data_type)

print(np_array)
