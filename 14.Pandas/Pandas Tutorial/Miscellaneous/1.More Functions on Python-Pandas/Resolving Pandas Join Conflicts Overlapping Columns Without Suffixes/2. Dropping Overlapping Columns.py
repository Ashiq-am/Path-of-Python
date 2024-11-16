df1_dropped = df1.drop(columns=['value'])
merged_df = pd.merge(df1_dropped, df2, on='key', how='inner')
print(merged_df)
