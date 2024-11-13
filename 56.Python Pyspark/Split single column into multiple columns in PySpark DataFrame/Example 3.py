# creating the row data for dataframe
data = [('Jaya', 'Sinha'), ('Milan', 'Soni'),
		('Rohit', 'Verma'), ('Maria', 'Anne'),
		('Jay', 'Mehta')]

# giving the column names for the dataframe
columns = ['First Name', 'Last Name']

# creating the dataframe df
df = spark.createDataFrame(data, columns)

# printing dataframe schema
df.printSchema()

# show dataframe
df.show()

# defining split()
split_cols = pyspark.sql.functions.split(df['Last Name'], '')

# applying split() using .withColumn()
df = df.withColumn('1', split_cols.getItem(0)) \
	.withColumn('2', split_cols.getItem(1)) \
	.withColumn('3', split_cols.getItem(2)) \
	.withColumn('4', split_cols.getItem(3)) \
	.withColumn('5', split_cols.getItem(4))

# show df
df.show()
