# Create another DataFrame with missing values
df2 = pd.DataFrame({
    'Age': [25, None, 22, None, 28],
    'Salary': [None, 55000, 40000, 70000, 48000]
}, index=['John', 'Alice', 'Bob', 'Eve', 'Charlie'])

# Combine the DataFrames using 'combine_first()'
combined_df = df2.combine_first(df)

# Display the combined DataFrame
print(combined_df)