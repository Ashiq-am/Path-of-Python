df1_renamed = df1.rename(columns={'value': 'value1'})
df2_renamed = df2.rename(columns={'value': 'value2'})

merged_df = pd.merge(df1_renamed, df2_renamed, on='key', how='inner')
print(merged_df)
