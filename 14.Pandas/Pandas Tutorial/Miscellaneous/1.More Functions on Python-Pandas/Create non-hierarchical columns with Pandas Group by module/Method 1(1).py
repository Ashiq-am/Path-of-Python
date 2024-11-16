df_result.columns = ['_'.join(cols).lower()
					for cols in df_result.columns.to_flat_index()]
df_result.head(10)
