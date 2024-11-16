# importing pandas package
import pandas as pd

# creating dataframe
values = {'Dates': [20190902093000, 20190913093000, 20190921200000],
		'Attendance': ['Attended', 'Not Attended', 'Attended']
		}

df = pd.DataFrame(values, columns=['Dates', 'Attendance'])

# changing integer values to datetime format
df['Dates'] = pd.to_datetime(df['Dates'], format='%Y%m%d%H%M%S')

# display
print(df)
print(df.dtypes)
