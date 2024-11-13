# Using select() to Add Multiple Column
df.select('*', (df.Runs / df.Matches).alias('Avg_runs'),
		(df.Wickets+10).alias('wkt+10')).show()
