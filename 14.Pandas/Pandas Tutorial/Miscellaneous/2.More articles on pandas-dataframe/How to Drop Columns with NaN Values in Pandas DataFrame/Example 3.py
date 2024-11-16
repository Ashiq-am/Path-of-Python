# Importing libraries
import pandas as pd
import numpy as np

# creating and initializing a nested list
age_list = [[np.nan, 1952, 8425333, np.nan, 28.35],
			['Australia', 1957, 9712569, 'Oceania', 24.26],
			['Brazil', 1962, 76039390, np.nan, 30.24],
			[pd.NaT, 1957, 637408000, 'Asia', 28.32],
			['France', 1957, 44310863, pd.NaT, 25.21],
			['India', 1952, 3.72e+08, pd.NaT, 27.36],
			['United States', 1957, 171984000, 'Americas', 28.98]]

# creating a pandas dataframe
df = pd.DataFrame(age_list, columns=[
				'Country', 'Year', 'Population', 'Continent', 'lifeExp'])

df
