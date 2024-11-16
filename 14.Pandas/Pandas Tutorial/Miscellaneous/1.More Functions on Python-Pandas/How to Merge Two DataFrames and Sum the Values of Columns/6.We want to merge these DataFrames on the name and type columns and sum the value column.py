# Perform the merge
merged_df = pd.merge(df1, df2, on=['name', 'type'], how='outer', suffixes=('_x', '_y'))

# Sum the values
merged_df['value'] = merged_df[['value_x', 'value_y']].sum(axis=1)

# Drop the intermediate columns
merged_df = merged_df.drop(columns=['value_x', 'value_y'])

print(merged_df)
