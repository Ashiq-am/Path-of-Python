import pandas as pd

# Creating dataframe
df1 = pd.DataFrame({'Name': ['rumul', 'rahul',
							'ravi', 'imran'],
					'Marks': [5, 20, 8, 12]})

df2 = pd.DataFrame({'Name': ['rumul', 'rahul',
							'purvi', 'ravi',
							'imran'],
					'Marks': [18, 19, 13, 11, 15]})

display(df1)
display(df2)

# replace values of one DataFrame with
# the value of another DataFrame
df1['Marks'] = df2[df2['Name'].isin(df1['Name'])]['Marks'].values

display(df1)
