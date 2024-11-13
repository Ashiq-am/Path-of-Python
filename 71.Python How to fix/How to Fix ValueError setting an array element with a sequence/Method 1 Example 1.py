# In this program we are demostraiting how different
# Data-type can cause value erro

import numpy

# Creating multi-dimension array
array1 = [1, 2, 4, [5, [6, 7]]]

# Data type of array element
Data_type = int

# This cause Value error
np_array = numpy.array(array1, dtype=Data_type)

print(np_array)
