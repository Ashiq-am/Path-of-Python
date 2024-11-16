# Accessing a column
print(df['Name'])

# Accessing a row by label
print(df.loc[0])

# Accessing a row by integer position
print(df.iloc[0])

# Accessing an individual element
print(df.at[0, 'Name'])
