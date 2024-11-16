# import python pandas package
import pandas as pd

# create a sample dataframe
data = pd.DataFrame({'cars': ['benz', 'benz', 'benz',
							'benz', 'bmw', 'bmw', 'bmw'],
					'Price_in_million': [15, 12, 23, 23, 63, 34, 63]})

# get the 4th row present in the data
data.iloc[4]

# Now apply lambda function to get the number
# of times the row is present in the dataset
data.apply(lambda x: sum(x==x.iloc[4]))
