# module to work with arrays in python
import array

# module required to compute power
import pandas as pd

# creating a 1-dimensional floating
# point array containing three elements
sample_array = array.array('d',
						[1.1, 2.0, 3.5])

# uni dimensional arrays can
# be mapped to pandas series
sr = pd.Series(sample_array)

print ("Original Array :")
print (sr)

# computing power of each
# element with itself
power_array = sr.pow(sr)

print ("Element-wise power array")
print (power_array)
