import functools
# explicit function


def unionAll(dfs):
	return functools.reduce(lambda df1, df2: df1.union(
	df2.select(df1.columns)), dfs)


# unionAll
result3 = unionAll([df1, df2])
result3.show()
