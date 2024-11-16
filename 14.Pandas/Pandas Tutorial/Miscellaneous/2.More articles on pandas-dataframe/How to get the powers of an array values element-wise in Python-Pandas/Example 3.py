# module to work with
# arrays in python
import array

# module required to
# compute power
import pandas as pd

# 2-d matrix containing
# 2 rows and 3 columns
df = pd.DataFrame({'X': [1,2],
				'Y': [3,4],
				'Z': [5,6]})

print ("Original Array :")
print(df)

# power function to calculate
# power of data frame elements
# with itself
power_array = df.pow(df)

print ("Element-wise power array")
print (power_array)
