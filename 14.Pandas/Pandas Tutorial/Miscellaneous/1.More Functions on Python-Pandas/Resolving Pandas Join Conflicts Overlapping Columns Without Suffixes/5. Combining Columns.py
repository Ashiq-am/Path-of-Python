merged_temp = pd.merge(df1, df2, on='key', how='outer')

merged_temp['value_combined'] = merged_temp['value_x'].combine_first(merged_temp['value_y'])
merged_df = merged_temp[['key', 'value_combined']]
print(merged_df)
