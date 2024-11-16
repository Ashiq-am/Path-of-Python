df = pd.concat([df1, df2])

df = df.reset_index(drop=True)

df_group = df.groupby(list(df.columns))

idx = [x[0] for x in df_group.groups.values() if len(x) > 1]
df.reindex(idx)
