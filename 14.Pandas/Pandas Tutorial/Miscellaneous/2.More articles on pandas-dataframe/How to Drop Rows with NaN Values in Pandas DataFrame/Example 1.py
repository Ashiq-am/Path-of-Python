# importing libraries
import pandas as pd
import numpy as np

num = {'Integers': [10, 15, 30, 40, 55, np.nan,
					75, np.nan, 90, 150, np.nan]}

# Create the dataframe
df = pd.DataFrame(num, columns =['Integers'])

# dropping the rows having NaN values
df = df.dropna()

# printing the result
df
