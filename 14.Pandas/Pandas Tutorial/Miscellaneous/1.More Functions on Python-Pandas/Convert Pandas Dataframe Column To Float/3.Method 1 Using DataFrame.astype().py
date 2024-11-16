# Print dtypes before conversion
print("Data types before conversion:")
print(df.dtypes)

# Convert 'StringColumn' to float using astype()
df['StringColumn'] = df['StringColumn'].astype(float)

# Print dtypes after conversion
print("\nData types after conversion:")
print(df.dtypes)

# Print the DataFrame
print("\nDataFrame after conversion:")
print(df)
