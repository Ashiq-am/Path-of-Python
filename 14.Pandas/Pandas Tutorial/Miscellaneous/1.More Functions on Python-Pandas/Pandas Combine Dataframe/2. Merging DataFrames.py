# Create another DataFrame to merge based on 'Name'
df2 = pd.DataFrame({
    'Name': ['John', 'Alice', 'Bob'],
    'Department': ['HR', 'IT', 'Finance']
})

# Merge DataFrames on the 'Name' column
merged_df = pd.merge(df, df2, on='Name', how='inner')

# Display the merged DataFrame
print(merged_df)