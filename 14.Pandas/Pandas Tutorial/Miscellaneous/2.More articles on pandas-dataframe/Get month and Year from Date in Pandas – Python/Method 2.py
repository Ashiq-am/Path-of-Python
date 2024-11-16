# import required library
import pandas as pd
import datetime as dt

# dictionary of string as key
# and list as a value
raw_data = {'Leaders': ['Mahatma Gandhi', 'Jawaharlal Nehru',
						'Atal Bihari Vajpayee', 'Rabindranath Tagore'],
			'birth_date': ['10-02-1869', '11-14-1889',
						'12-25-1924', '05-07-1861']}

# create a dataframe object
df = pd.DataFrame(raw_data,
				index = ['Mahatma Gandhi', 'Jawaharlal Nehru',
						'Atal Bihari Vajpayee',
						'Rabindranath Tagore'])

# get a year from corresponding
# birth_date column value
df['year'] = df['birth_date'].dt.year

# get a month from corresponding
# birth_date column value
df['month'] = df['birth_date'].dt.month

# show the dataframe
# by default first 5 rows
# from top
df.head()
