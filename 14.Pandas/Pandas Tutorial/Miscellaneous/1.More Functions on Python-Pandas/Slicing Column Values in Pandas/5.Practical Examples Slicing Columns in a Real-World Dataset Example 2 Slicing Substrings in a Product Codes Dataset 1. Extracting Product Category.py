# Slice the first character to get the product category
df['Category'] = df['ProductCode'].str.slice(0, 1)
print(df)
