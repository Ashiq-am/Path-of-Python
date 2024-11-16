new = df.groupby(['States','Products'],as_index = False
				).count().pivot('States','Products').fillna(0)
display(new)
