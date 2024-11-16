# using keys from left frame
res = pd.merge(df, df1, how='left', on=['key', 'key1'])

res
