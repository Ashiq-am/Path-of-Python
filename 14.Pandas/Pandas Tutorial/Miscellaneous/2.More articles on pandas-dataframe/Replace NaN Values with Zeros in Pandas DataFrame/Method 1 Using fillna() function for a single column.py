# importing libraries
import pandas as pd
import numpy as np

nums = {'Set_of_Numbers': [2, 3, 5, 7, 11, 13,
						np.nan, 19, 23, np.nan]}

# Create the dataframe
df = pd.DataFrame(nums, columns =['Set_of_Numbers'])

# Apply the function
df['Set_of_Numbers'] = df['Set_of_Numbers'].fillna(0)

# print the DataFrame
df
