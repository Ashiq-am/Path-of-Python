# Python program for demonstrating
# the use of fields
import numpy as np

# A structured data type containing a
# 16-character string (in field ‘name’)
# and a sub-array of two 64-bit floating
# -point number (in field ‘grades’)

dt = np.dtype([('name', np.unicode_, 16),
               ('grades', np.float64, (2,))])

# Data type of object with field grades
print(dt['grades'])

# Data type of object with field name
print(dt['name'])