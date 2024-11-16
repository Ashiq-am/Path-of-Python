# Apply any custom function
def summation(col):
	if col.dtypes != 'int64':
		return col.count()
	else:
		return col.sum()


df.apply(summation)
