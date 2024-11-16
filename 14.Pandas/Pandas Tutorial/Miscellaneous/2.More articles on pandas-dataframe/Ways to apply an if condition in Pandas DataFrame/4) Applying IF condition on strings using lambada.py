from pandas import DataFrame

names = {'First_name': ['Hanah', 'Ria', 'Jay', 'Bholu', 'Sachin']}
df = DataFrame(names, columns =['First_name'])

df['Status'] = df['First_name'].apply(lambda x: 'Found' if x == 'Ria' else 'Not Found')

print (df)
