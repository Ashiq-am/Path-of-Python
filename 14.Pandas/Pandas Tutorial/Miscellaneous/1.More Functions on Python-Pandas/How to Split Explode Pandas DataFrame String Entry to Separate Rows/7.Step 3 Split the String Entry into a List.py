#split the data column on ', '
df['data'] = df['data'].str.split(', ')
#print dataframe
print(df)
