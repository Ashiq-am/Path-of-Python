# Perform a left join on 'Name'
left_joined_df = pd.merge(df1, df2, on='Name', how='left')
print(left_joined_df)