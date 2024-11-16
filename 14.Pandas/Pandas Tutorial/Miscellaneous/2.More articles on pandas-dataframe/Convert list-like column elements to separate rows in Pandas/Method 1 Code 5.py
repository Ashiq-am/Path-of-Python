df_melt = df.assign(names=df.names.str.split(","))
df_melt = df_melt.names.apply(pd.Series) \
	.merge(df_melt, right_index=True, left_index=True) \
	.drop(["names"], axis=1) \
	.melt(id_vars=['id'], value_name="names") \
	.drop("variable", axis=1) \
	.dropna()

print(df_melt)
