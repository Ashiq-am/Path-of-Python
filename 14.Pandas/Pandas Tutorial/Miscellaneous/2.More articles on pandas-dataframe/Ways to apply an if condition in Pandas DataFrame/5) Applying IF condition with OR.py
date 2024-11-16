from pandas import DataFrame

names = {'First_name': ['Hanah', 'Ria', 'Jay', 'Bholu', 'Sachin']}
df = DataFrame(names, columns =['First_name'])

df.loc[(df['First_name'] == 'Ria') | (df['First_name'] == 'Jay'), 'Status'] = 'Found'
df.loc[(df['First_name'] != 'Ria') & (df['First_name'] != 'Jay'), 'Status'] = 'Not Found'

print (df)
