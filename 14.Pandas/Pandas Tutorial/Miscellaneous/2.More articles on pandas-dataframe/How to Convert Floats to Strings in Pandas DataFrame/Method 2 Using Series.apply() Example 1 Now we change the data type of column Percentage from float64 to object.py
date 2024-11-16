# Now we will convert it from
# 'float' to 'string' type.
df['Percentage'] = df['Percentage'].apply(str)
print()

# lets find out the data
# type after changing
print(df.dtypes)

# print dataframe.
df
