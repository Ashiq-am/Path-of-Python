# importing package
import numpy
import pandas

# string "deep" is not nan value
print(pandas.isna("deep"))

# numpy.nan represents a nan value
print(pandas.isna(numpy.nan))
