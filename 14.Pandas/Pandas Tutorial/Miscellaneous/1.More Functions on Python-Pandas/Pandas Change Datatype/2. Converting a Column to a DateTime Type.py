# Example: Create a 'Join Date' column as a string
df['Join Date'] = ['2021-01-01', '2020-05-22', '2022-03-15', '2021-07-30', '2020-11-11']

# Convert 'Join Date' to datetime type
df['Join Date'] = pd.to_datetime(df['Join Date'])
print(df.dtypes)