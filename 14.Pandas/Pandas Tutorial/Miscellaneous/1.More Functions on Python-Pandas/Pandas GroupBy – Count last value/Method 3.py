# import pandas package
import pandas as pd
# create a sample dataset
data = pd.DataFrame({'cars': ['benz', 'benz', 'benz',
							'benz', 'bmw', 'bmw', 'bmw'],
					'Price_in_million': [15, 12, 23, 23, 63, 34, 63]})

# perform inner merge with the grouped and original dataset
merged = pd.merge(data.groupby('cars').tail(1), data, how='inner')

# apply a count aggreagated groupby function to
# get the no. of. occurrences of last value.
result = merged.groupby(['cars', 'Price_in_million'])[
	'Price_in_million'].agg('count')
print(result)
