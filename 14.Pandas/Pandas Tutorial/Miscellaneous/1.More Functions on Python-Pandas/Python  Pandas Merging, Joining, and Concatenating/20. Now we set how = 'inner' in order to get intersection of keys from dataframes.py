# getting intersection of keys
res3 = pd.merge(df, df1, how='inner', on=['key', 'key1'])

res3
