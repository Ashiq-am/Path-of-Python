# Drop both 'Age' and 'Gender' columns
df = df.drop(['Age', 'Gender'], axis=1)
print(df)