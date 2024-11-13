new_df = df.withColumn(
	'Hundred_run', df.Hundreds*100).withColumn(
	'Avg_run', df.Runs / df.Matches)

new_df.show()
