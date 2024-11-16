# importing pandas package
import pandas as pd

# creating the dataframe
values = {'Dates': [20190902, 20190913, 20190921],
		'Attendance': ['Attended', 'Not Attended', 'Attended']
		}

df = pd.DataFrame(values, columns=['Dates', 'Attendance'])

# converting the integers to datetime format
df['Dates'] = pd.to_datetime(df['Dates'], format='%Y%m%d')

# display
print(df)
print(df.dtypes)
