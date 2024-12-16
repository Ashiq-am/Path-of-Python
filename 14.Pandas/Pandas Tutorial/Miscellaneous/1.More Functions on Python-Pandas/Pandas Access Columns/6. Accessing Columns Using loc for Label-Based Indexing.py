# Access 'Age' and 'Gender' columns for rows where 'Salary' is greater than 50000
filtered_data = df.loc[df['Salary'] > 50000, ['Age', 'Gender']]
print(filtered_data)