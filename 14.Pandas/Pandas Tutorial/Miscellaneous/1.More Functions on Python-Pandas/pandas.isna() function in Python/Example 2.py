# importing package
import numpy
import pandas

# create and view data
array = numpy.array([[1, numpy.nan, 3],
					[4, 5, numpy.nan]])

print(array)

# numpy.nan represents a nan value
print(pandas.isna(array))
