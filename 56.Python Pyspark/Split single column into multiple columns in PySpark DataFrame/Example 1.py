# split() function defining parameters
split_cols = pyspark.sql.functions.split(df['DOB'], '-')

# Now applying split() using withColumn()
df1 = df.withColumn('Year', split_cols.getItem(0)) \
	.withColumn('Month', split_cols.getItem(1)) \
	.withColumn('Day', split_cols.getItem(2))

# show df
df1.show()
