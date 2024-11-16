from pandas import DataFrame

numbers = {'mynumbers': [51, 52, 53, 54, 55]}
df = DataFrame(numbers, columns =['mynumbers'])

df.loc[df['mynumbers'] <= 53, '<= 53'] = 'True'
df.loc[df['mynumbers'] > 53, '<= 53'] = 'False'

df
