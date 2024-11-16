# import python pandas package
import pandas as pd

# create a sample dataframe
data = pd.DataFrame({'cars': ['benz', 'benz', 'benz',
							'benz', 'bmw', 'bmw', 'bmw'],
					'Price_in_million': [15, 12, 23, 23,
										63, 34, 63]})


# use groupby function to groupby cars, setting
# as_index false doesnt create an index.
# use aggregate function with 'last; parameter
# to get the last price im the group of cars.
# apply lambda function to get the number of
# times the car got the last price.
data.groupby('cars', as_index=False).agg(Price_last=('Price_in_million', 'last'),
										Price_last_count=('Price_in_million',
														lambda x: sum(x == x.iloc[-1])))
