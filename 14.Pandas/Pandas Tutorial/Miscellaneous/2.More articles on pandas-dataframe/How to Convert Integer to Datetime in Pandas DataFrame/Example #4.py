# importing pandas package
import pandas as pd

# creating dataframe
values = {'Dates': [20190902093000912, 20190913093000444,
					20190921200000009],
		'Attendance': ['Attended', 'Not Attended', 'Attended']
		}

df = pd.DataFrame(values, columns=['Dates', 'Attendance'])

# changing the integer dates to datetime format
df['Dates'] = pd.to_datetime(df['Dates'], format='%Y%m%d%H%M%S%F')

# display
print(df)
print(df.dtypes)
