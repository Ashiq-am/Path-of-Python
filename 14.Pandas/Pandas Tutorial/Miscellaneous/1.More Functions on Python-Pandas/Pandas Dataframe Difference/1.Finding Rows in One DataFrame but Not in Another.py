# Merge the DataFrames with the 'indicator' flag to track the source of each row
merged_df = pd.merge(df1, df2, how='outer', indicator=True)

# Find rows that are only in df1 but not in df2
diff_df1 = merged_df[merged_df['_merge'] == 'left_only']
print(diff_df1)

# Find rows that are only in df2 but not in df1
diff_df2 = merged_df[merged_df['_merge'] == 'right_only']
print(diff_df2)