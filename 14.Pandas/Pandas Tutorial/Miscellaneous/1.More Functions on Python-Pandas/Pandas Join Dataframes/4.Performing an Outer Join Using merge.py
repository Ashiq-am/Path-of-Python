# Perform an outer join on 'Name'
outer_joined_df = pd.merge(df1, df2, on='Name', how='outer')
print(outer_joined_df)