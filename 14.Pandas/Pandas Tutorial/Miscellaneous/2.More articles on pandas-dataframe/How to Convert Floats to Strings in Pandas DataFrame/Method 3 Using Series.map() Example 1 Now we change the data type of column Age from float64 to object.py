# Now we will convert it from 'float' to 'string' type.
# using DataFrame.map(str) function
df['Age'] = df['Age'].map(str)
print()

# lets find out the data type after changing
print(df.dtypes)

# print dataframe.
df
