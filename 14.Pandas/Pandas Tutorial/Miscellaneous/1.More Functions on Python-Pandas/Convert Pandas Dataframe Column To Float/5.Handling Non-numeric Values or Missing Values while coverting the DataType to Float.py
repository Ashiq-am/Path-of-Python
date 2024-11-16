# Sample DataFrame with non-numeric and missing values
data = {'Column1': ['10.5', '20.7', '30.2', 'xyz'],
		'Column2': ['15.3', '25.6', '35.8', '']}
df = pd.DataFrame(data)

print('Original DataFrame')
print(df)

# Convert columns to float, handling errors and missing values
df['Column1'] = pd.to_numeric(df['Column1'], errors='coerce')
df['Column2'] = pd.to_numeric(df['Column2'], errors='coerce')

# Print dtypes after conversion
print("\nData types after conversion:")
print(df.dtypes)

# Print the DataFrame
print("\nDataFrame after conversion:")
print(df)
