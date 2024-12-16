# Convert 'Age' column to float type
df['Age'] = df['Age'].astype(float)
print(df.dtypes)