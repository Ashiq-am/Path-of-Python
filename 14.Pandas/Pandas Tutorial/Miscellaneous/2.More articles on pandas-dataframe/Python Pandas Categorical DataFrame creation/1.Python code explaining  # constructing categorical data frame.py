# Python code explaining
# constructing categorical data frame

# importing libraries
import numpy as np
import pandas as pd

# Constructing dataframe
data = {'col1': [1, 2, 4, 5], 'col2': [3, 4, 5, 6]}
df1 = pd.DataFrame(data = data)

print ("df1 : \n", df1)
print("\n\ndf1 type :\n", df1.dtypes)
