# importing libraries
import pandas as pd
import numpy as np

nums = {'Student Number': [ 1001, 1111, 1202, 1229, 1330,
						1335, np.nan, 1400, 1150, np.nan],
		'Seat Number': [np.nan, 15, 22, 43, np.nan, 44,
						55, np.nan, 57, np.nan]}

# Create the dataframe
df = pd.DataFrame(nums, columns =['Student Number', 'Seat Number'])

# dropping the rows having NaN values
df = df.dropna()

# To reset the indices
df = df.reset_index(drop = True)

# Print the dataframe
df
