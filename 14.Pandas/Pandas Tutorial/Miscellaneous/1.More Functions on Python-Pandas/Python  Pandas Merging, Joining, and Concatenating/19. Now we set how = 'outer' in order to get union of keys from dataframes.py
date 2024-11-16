# getting union  of keys
res2 = pd.merge(df, df1, how='outer', on=['key', 'key1'])

res2
