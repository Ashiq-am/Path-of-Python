# Example: Group by 'Gender' and 'Age' (creating an age range)
df['Age Group'] = pd.cut(df['Age'], bins=[20, 25, 30, 35, 40], labels=['20-25', '26-30', '31-35', '36-40'])

# Group by 'Gender' and 'Age Group', then calculate the average Salary
grouped_df = df.groupby(['Gender', 'Age Group'])['Salary'].mean()
print(grouped_df)