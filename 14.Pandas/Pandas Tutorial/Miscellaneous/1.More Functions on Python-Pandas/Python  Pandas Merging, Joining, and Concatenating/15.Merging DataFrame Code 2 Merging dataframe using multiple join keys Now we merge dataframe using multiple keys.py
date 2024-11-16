# merging dataframe using multiple keys
res1 = pd.merge(df, df1, on=['key', 'key1'])

res1
