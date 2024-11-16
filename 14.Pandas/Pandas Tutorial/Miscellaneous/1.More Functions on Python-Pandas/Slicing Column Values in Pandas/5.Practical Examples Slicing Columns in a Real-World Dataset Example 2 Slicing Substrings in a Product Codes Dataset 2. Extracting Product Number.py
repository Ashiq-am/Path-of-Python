# Slice the numeric part of the product code
df['ProductNumber'] = df['ProductCode'].str.slice(1)
print(df)
