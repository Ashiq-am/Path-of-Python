# Merge df1 and df2 on the 'Name' column
merged_df = pd.merge(df1, df2, on='Name', how='inner')
print(merged_df)