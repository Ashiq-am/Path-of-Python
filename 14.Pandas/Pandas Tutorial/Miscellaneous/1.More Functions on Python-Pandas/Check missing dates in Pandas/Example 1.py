#import pandas
import pandas as pd

# A dataframe from a dictionary of lists
data = {'Date': ['2021-01-18', '2021-01-20',
				'2021-01-23', '2021-01-25'],
		'Name': ['Jia', 'Tanya', 'Rohan', 'Sam']}
df = pd.DataFrame(data)

# Setting the Date values as index
df = df.set_index('Date')

# to_datetime() method converts string
# format to a DateTime object
df.index = pd.to_datetime(df.index)

# dates which are not in the sequence
# are returned
print(pd.date_range(
start="2021-01-18", end="2021-01-25").difference(df.index))
