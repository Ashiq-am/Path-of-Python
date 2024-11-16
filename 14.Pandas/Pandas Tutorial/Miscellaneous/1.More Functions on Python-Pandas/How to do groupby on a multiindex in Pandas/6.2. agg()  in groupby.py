# performing max() and min() operation,
# on the 'state_pop' column.
df_agg = df.groupby(
level=["region", "state"])["state_pop"].agg(["max", "min"])

print(df_agg)
