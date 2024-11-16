# import pamdas library
import pandas as pd


# dictionary of string key and list value
raw_data = {'name': ['Rutuja', 'Neeraj',
					'Renna', 'Pratik'],
			'age': [20, 19, 22, 21],
			'favorite_color': ['blue', 'red',
							'yellow', "green"],
			'grade': [88, 92, 95, 70],
			'birth_date': ['01-02-2000', '08-05-1997',
						'04-28-1996', '12-16-1995']}

# create a dataframe object
df = pd.DataFrame(raw_data,
				index = ['Rutuja', 'Neeraj',
						'Renna', 'Pratik'])

# get year from the corresponding
# birth_date column value
df['year'] = pd.DatetimeIndex(df['birth_date']).year

# get month from the corresponding
# birth_date column value
df['month'] = pd.DatetimeIndex(df['birth_date']).month

# Show the dataframe
# by default 5 rows from top
df.head()
