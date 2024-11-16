# Storing in a New DataFrame
filtered_df = df[df > 30]

# Writing to a CSV File
filtered_df.to_csv('filtered_columns.csv', index=False)
