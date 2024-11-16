Mean = df.DISCOUNT.mean()

# Fill the null values
df['DISCOUNT'] = df['DISCOUNT'].fillna(Mean)
print(df)
