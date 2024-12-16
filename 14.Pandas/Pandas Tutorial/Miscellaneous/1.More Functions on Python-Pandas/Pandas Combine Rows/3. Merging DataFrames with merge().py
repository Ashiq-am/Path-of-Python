# Create another DataFrame with some overlapping data
df2 = pd.DataFrame({
    'Name': ['John', 'Alice', 'Bob'],
    'Department': ['HR', 'IT', 'Finance']
})

# Merge the two DataFrames based on the 'Name' column
merged_df = pd.merge(df, df2, on='Name', how='inner')

# Display the merged DataFrame
print(merged_df)