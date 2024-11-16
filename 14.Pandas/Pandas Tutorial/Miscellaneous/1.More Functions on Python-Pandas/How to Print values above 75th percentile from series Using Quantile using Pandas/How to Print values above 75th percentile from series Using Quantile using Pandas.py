# importing pandas module
import pandas as pd

# importing numpy module
import numpy as np

# Making an array
arr = np.array([42, 12, 72, 85, 56, 100])

# creating a series
Ser1 = pd.Series(arr)

# printing this series
print(Ser1)

# calculating quantile/percentile value
quantile_value = Ser1.quantile(q=0.75)

# printing quantile/percentile value
print("75th Percentile is:", quantile_value)
print("Values that are greater than 75th percentile are:")

# Running a loop and
# printing all elements that are above the
# 75th percentile
for val in Ser1:
	if (val > quantile_value):
		print(val)
