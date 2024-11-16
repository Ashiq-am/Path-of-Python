import pandas as pd
from pandas import DataFrame

# creating a dictionary of names
Names = {'FirstName':['Suzie','Emily','Mike','Robert'],
		'LastName':['Bates','Edwards','Curry','Frost']}

# creating a dataframe from dictionary
df = DataFrame(Names, columns=['FirstName','LastName'])
print(df)

print('\n')

# concatenating the columns
df['Name'] = df['FirstName'].map(str) + ' ' + df['LastName'].map(str)
print(df)
