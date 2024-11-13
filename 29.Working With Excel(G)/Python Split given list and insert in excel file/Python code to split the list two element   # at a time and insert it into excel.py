# Python code to split the list two element
# at a time and insert it into excel.

# Importing pandas as pd
import pandas as pd

# List initialization
list1 = ['Assam', 'India',
		'Lahore', 'Pakistan',
		'New York', 'USA',
		'Bejing', 'China']

df = pd.DataFrame()

# Creating two columns
df['State'] = list1[0::2]
df['Country'] = list1[1::2]

# Converting to excel
df.to_excel('result.xlsx', index = False)