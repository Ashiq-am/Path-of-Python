import numpy as np
dtype = np.dtype([('integer_field', np.int32), ('float_field', np.float64), ('string_field', 'U10')])
# Create a record array with different data types
record_array = np.array([(1, 1.5, 'one'), (2, 2.5, 'two'), (3, 3.5, 'three')], dtype=dtype)
print(record_array)
print(record_array.dtype)
