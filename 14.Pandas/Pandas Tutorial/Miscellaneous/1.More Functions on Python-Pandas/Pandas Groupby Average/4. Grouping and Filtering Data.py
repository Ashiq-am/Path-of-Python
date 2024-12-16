# Group by 'Gender' and calculate the average Salary
grouped_df = df.groupby('Gender')['Salary'].mean()

# Filter to get only those with average salary greater than 50000
filtered_df = grouped_df[grouped_df > 50000]
print(filtered_df)