def dropNullColumns(df):
	"""
	This function drops columns containing all null values.
	:param df: A PySpark DataFrame
	"""

	null_counts = df.select([sqlf.count(sqlf.when(sqlf.col(c).isNull(), c)).alias(
		c) for c in df.columns]).collect()[0].asDict() # 1
	col_to_drop = [k for k, v in null_counts.items() if v > 0] # 2
	df = df.drop(*col_to_drop) # 3

	return df
