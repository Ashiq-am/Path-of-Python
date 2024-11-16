# importing pandas package
import pandas as pd

# creating a dataframe
values = {'Dates': [20190902, 20190913, 20190921],
		'Attendance': ['Attended', 'Not Attended', 'Attended']
		}

df = pd.DataFrame(values, columns=['Dates', 'Attendance'])

# display
print(df)
print(df.dtypes)
