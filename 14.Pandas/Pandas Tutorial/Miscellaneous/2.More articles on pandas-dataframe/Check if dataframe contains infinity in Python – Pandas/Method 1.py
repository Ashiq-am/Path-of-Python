# Import required libraries

import pandas as pd
import numpy as np

# Create dataframe using dictionary
from IPython.core.display import display

data = {'Student ID': [10, 11, 12, 13, 14],
		'Age': [23, 22, 24, 22, 25],
		'Weight': [66, 72, np.inf, 68, -np.inf]}

df = pd.DataFrame(data)

display(df)

# checking for infinity
print()
print("checking for infinity")

ds = df.isin([np.inf, -np.inf])
print(ds)

# printing the count of infinity values
print()
print("printing the count of infinity values")

count = np.isinf(df).values.sum()
print("It contains " + str(count) + " infinite values")

# counting infinity in a particular column name
c = np.isinf(df['Weight']).values.sum()
print("It contains " + str(c) + " infinite values")

# printing column name where infinity is present
print()
print("printing column name where infinity is present")
col_name = df.columns.to_series()[np.isinf(df).any()]
print(col_name)

# printing row index with infinity
print()
print("printing row index with infinity ")

r = df.index[np.isinf(df).any(1)]
print(r)
