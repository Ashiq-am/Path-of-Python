# Now we will convert it from
# 'float' to 'String' type.
df['Marks'] = df['Marks'].astype(str)

print()

# lets find out the data
# type after changing
print(df.dtypes)

# print dataframe.
df
