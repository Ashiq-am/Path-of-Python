# Sample DataFrame
data = {'C1': ['10.5', '20.7', '30.2'],
		'C2': ['15.3', '25.6', '35.8']}
df = pd.DataFrame(data)

# Print dtypes before conversion
print("Data types before conversion:")
print(df.dtypes)

# Convert multiple columns to float using astype()
df[['C1', 'C2']] = df[['C1', 'C2']].astype(float)

# Print dtypes after conversion
print("\nData types after conversion:")
print(df.dtypes)

# Print the DataFrame
print("\nDataFrame after conversion:")
print(df)
