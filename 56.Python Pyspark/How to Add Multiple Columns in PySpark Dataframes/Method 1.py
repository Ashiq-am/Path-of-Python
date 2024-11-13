df.withColumn(
	'Avg_runs', df.Runs / df.Matches).withColumn(
	'wkt+10', df.Wickets+10).show()
