# Define the schema
schema = StructType([
	StructField("id", IntegerType(), True),
	StructField("name", StringType(), True),
	StructField("age", IntegerType(), True)
])
