# importing pandas and numpy
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10, 4),
		columns = ['A', 'B', 'C', 'D'])

print("Original DataFrame: \n" , df)

# Integer slicing
print("\n Slicing only rows:")
print("--------------------------")
x1 = df.ix[:4, ]
print(x1)

print("\n Slicing rows and columns:")
print("----------------------------")
x2 = df.ix[:4, 1:3]
print(x2)
