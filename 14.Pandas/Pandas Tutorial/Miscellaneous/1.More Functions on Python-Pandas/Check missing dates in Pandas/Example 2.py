#import pandas
import pandas as pd

# A dataframe from a dictionary of lists
d = {'Date': ['2021-01-10', '2021-01-14', '2021-01-18',
			'2021-01-25', '2021-01-28', '2021-01-29'],
	'Total People': [20, 21, 19, 18, 13, 56]}
df = pd.DataFrame(d)

# Setting the Totale People as index
df = df.set_index('Total People')

# to_datetime() method converts string
# format to a DateTime object
df['Date'] = pd.to_datetime(df['Date'])

# dates which are not in the sequence
# are returned
my_range = pd.date_range(
start="2021-01-10", end="2021-01-31", freq='B')

print(my_range.difference(df['Date']))
