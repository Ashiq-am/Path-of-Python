from pandas import DataFrame

numbers = {'mynumbers': [51, 52, 53, 54, 55]}
df = DataFrame(numbers, columns =['mynumbers'])

df['<= 53'] = df['mynumbers'].apply(lambda x: 'True' if x <= 53 else 'False')

print (df)
