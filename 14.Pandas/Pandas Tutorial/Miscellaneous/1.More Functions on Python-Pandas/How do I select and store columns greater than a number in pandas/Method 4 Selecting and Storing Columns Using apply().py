# Applying a condition using apply()
df_mean_greater_than_30 = df.loc[:, df.apply(lambda col: col.mean() > 30)]
print(df_mean_greater_than_30)
