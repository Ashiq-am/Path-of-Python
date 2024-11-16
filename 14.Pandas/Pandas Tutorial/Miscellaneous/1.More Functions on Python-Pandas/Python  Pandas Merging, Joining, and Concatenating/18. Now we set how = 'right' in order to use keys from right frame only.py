# using keys from right frame
res1 = pd.merge(df, df1, how='right', on=['key', 'key1'])

res1
