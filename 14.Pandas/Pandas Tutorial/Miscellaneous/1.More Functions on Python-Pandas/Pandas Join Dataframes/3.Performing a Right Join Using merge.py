# Perform a right join on 'Name'
right_joined_df = pd.merge(df1, df2, on='Name', how='right')
print(right_joined_df)