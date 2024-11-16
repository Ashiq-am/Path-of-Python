# Now we will convert it from 'int' to 'float' type
# using pandas.to_numeric()
df['Weight'] = pd.to_numeric(df['Weight'], downcast='float')
print()

# lets find out the data type after changing
print(df.dtypes)

# print dataframe.
df
