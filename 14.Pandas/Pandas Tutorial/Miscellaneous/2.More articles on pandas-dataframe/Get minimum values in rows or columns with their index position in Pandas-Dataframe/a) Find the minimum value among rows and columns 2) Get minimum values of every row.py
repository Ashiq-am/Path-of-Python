# import pandas library
import pandas as pd

# list of Tuples
data = [
		(20, 16, 23),
		(30, None, 11),
		(40, 34, 11),
		(50, 35, None),
		(60, 40, 13)
		]

# creating a DataFrame object
df = pd.DataFrame(data, index = ['a', 'b', 'c', 'd', 'e'],
					columns = ['x', 'y', 'z'])

# getting a series object containing
# minimum value from each row
# of given dataframe
minvalue_series = df.min(axis = 1)

minvalue_series
