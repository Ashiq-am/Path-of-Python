# Import required libraries
import pandas as pd
import numpy as np

# Dictionary
df1 = {
	'Name': ['abc', 'bcd', 'cde',
			'def', 'efg', 'fgh',
			'ghi'],
	'Math_score': [52, 87, 49,
				74, 28, 59,
				48]}

# Create a DataFrame
df1 = pd.DataFrame(df1,
				columns = ['Name',
							'Math_score'])

# Calculating Percentage
df1['percent'] = (df1['Math_score'] /
				df1['Math_score'].sum()) * 100

# Show the dataframe
df1
