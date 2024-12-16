# Group by 'Gender' and calculate the average salary and age
grouped_df = df.groupby('Gender').mean()
print(grouped_df)