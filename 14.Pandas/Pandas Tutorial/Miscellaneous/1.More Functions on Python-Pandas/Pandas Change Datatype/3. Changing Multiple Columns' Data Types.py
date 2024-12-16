# Convert 'Age' to float and 'Salary' to string
df = df.astype({'Age': 'float64', 'Salary': 'str'})
print(df.dtypes)