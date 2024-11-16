# Now we will convert it from 'int' to 'float' type
# using DataFrame.astype() function
df['Weight'] = df['Weight'].astype(float)

print()

# lets find out the data type after changing
print(df.dtypes)

# print dataframe.
df
