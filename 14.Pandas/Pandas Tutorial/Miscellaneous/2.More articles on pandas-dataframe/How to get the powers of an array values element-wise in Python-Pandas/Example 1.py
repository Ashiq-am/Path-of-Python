# import required modules
import numpy as np
import pandas as pd

# create an array
sample_array = np.array([1, 2, 3])

# uni dimensional arrays can be
# mapped to pandas series
sr = pd.Series(sample_array)

print ("Original Array :")
print (sr)

# calculating element-wise power
power_array = sr.pow(sr)

print ("Element-wise power array")
print (power_array)
