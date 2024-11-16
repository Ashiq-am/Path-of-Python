# importing pandas and numpy
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10, 4),
		columns = ['A', 'B', 'C', 'D'])

print("Original DataFrame: \n" , df)

# Integer slicing (printing all the rows of column 'A')
print("\n After index slicing (On 'A'):")
print("--------------------------")
x = df.ix[:, 'A']

print(x)
