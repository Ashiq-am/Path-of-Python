# Set 'Name' as the index for both DataFrames
df1.set_index('Name', inplace=True)
df2.set_index('Name', inplace=True)

# Join df1 with df2 on the index
joined_df = df1.join(df2)
print(joined_df)