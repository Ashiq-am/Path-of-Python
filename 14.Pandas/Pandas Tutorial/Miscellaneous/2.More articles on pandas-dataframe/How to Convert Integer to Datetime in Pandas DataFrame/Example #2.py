# importing pandas package
import pandas as pd

# creating dataframe
values = {'Dates': [190902, 190913, 190921],
		'Attendance': ['Attended', 'Not Attended', 'Attended']
		}

df = pd.DataFrame(values, columns=['Dates', 'Attendance'])

# changing the integer dates to datetime format
df['Dates'] = pd.to_datetime(df['Dates'], format='%y%m%d')

# display
print(df)
print(df.dtypes)
