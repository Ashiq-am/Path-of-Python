# Find rows in df1 that are not in df2
df_diff = df1[~df1['Name'].isin(df2['Name'])]
print(df_diff)