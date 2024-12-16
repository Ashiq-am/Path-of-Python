# Group by 'Gender' and calculate multiple statistics for Salary
grouped_df = df.groupby('Gender')['Salary'].agg(['mean', 'sum', 'count'])
print(grouped_df)