# import pandas package
import pandas as pd

# create a sample dataset
data = pd.DataFrame({'cars': ['benz', 'benz', 'benz',
							'benz', 'bmw', 'bmw', 'bmw'],
				'Price_in_million': [15, 12, 23, 23, 63, 34, 63]})

# computes the final value of each group
grouped = data.groupby('cars').last()

# Merge dataset named "data" with this result
data = data.merge(grouped, left_on='cars', right_index=True, how='inner')

# Now compare the merged columns for same price
# and create a new column of boolean values
# where prices match
data['count'] = data['Price_in_million_x'] == data['Price_in_million_y']

# Use groupby function to return the aggreated
# sum of count column where the price matches
data.groupby('cars')['count'].sum()
