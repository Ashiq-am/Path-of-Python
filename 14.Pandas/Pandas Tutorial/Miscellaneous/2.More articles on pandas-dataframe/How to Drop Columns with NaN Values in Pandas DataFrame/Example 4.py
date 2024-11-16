# Importing libraries
import pandas as pd
import numpy as np

# Creating a dictionary
dit = {'August': [10, np.nan, 34, 4.85, 71.2, 1.1],
	'September': [np.nan, 54, 68, 9.25, pd.NaT, 0.9],
		'October': [np.nan, 5.8, 8.52, np.nan, 1.6, 11],
	'November': [pd.NaT, 5.8, 50, 8.9, 77, pd.NaT] }

# Converting it to data frame
df = pd.DataFrame(data=dit)

# data frame
df
