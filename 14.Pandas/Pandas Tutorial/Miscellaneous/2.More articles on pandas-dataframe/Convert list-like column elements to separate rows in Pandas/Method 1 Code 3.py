df_melt.names.apply(pd.Series) \
	.merge(df_melt, right_index = True, left_index = True)
