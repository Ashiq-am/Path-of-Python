# Now we will convert them from 'int' to 'float' type
# using pandas.to_numeric()
df['Experience'] = pd.to_numeric(df['Experience'], downcast='float')
df['Height'] = pd.to_numeric(df['Height'], downcast='float')

print()

# lets find out the data type after changing
print(df.dtypes)

# print dataframe.
df
