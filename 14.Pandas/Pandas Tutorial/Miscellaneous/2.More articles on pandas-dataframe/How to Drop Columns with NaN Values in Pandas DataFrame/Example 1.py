# Importing libraries
import pandas as pd
import numpy as np

# Creating a dictionary
dit = {'August': [pd.NaT, 25, 34, np.nan, 1.1, 10],
	'September': [4.8, pd.NaT, 68, 9.25, np.nan, 0.9],
	'October': [78, 5.8, 8.52, 12, 1.6, 11], }

# Converting it to data frame
df = pd.DataFrame(data=dit)

# DataFrame
df
