# importing libraries
import pandas as pd
import numpy as np

nums = {'Integers_1': [10, 15, 30, 40, 55, np.nan, 75,
					np.nan, 90, 150, np.nan],
		'Integers_2': [np.nan, 21, 22, 23, np.nan, 24, 25,
					np.nan, 26, np.nan, np.nan]}

# Create the dataframe
df = pd.DataFrame(nums, columns=['Integers_1', 'Integers_2'])

# applying the method
nan_in_df = df.isnull().values.any()

# Print the dataframe
print(nan_in_df)
