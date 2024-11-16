# Drop the listed columns
df_view = df[df.columns.difference(['Position', 'Age', 'Salary'])]

# Print the new DataFrame
print(df_view)
