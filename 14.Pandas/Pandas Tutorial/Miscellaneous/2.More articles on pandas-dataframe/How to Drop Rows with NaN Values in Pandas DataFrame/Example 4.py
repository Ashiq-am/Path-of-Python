# importing libraries
import pandas as pd
import numpy as np

car = {'Year of Launch': [ 1999, np.nan, 1986, 2020, np.nan,
						1991, 2007, 2011, 2001, 2017],
		'Engine Number': [np.nan, 15, 22, 43, 44, np.nan,
							55, np.nan, 57, np.nan],
		'Chasis Unique Id': [4023, np.nan, 3115, 4522, 3643,
							3774, 2955, np.nan, 3587, np.nan]}

# Create the dataframe
df = pd.DataFrame(car, columns =['Year of Launch', 'Engine Number',
								'Chasis Unique Id'])

# dropping the rows having NaN values
df = df.dropna()

# To reset the indices
df = df.reset_index(drop = True)

# Print the dataframe
df
