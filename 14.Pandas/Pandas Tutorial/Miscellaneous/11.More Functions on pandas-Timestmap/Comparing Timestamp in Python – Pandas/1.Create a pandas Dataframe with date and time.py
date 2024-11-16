import pandas as pd

# Create a dataframe
df = pd.DataFrame({
	'year': [2017, 2017, 2017, 2018, 2018],
	'month': [11, 11, 12, 1, 2],
	'day': [29, 30, 31, 1, 2],
	'hour': [10, 10, 10, 11, 11],
	'minute': [10, 20, 25, 30, 40]})

def time(rows):
	return (pd.Timestamp(rows.year, rows.month,
						rows.day, rows.hour, rows.minute))

# Create new column with entries of date
# and time provided in timestamp format
df['new_time'] = df.apply(time, axis = 'columns')
display(df)
