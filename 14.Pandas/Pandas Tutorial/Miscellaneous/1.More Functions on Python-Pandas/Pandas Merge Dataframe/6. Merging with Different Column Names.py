# Rename 'ID' in df2 to 'EmployeeID' for demonstration
df2.rename(columns={'ID': 'EmployeeID'}, inplace=True)

# Merge using different column names
merged_df = pd.merge(df1, df2, left_on='ID', right_on='EmployeeID', how='inner')
print(merged_df)