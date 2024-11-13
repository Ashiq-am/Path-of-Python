from pyspark.sql.types import StructType, StructField, StringType, IntegerType

# Define the schema for the DataFrame
schema = StructType([
	StructField("name", StringType()),
	StructField("age", IntegerType()),
	StructField("address", StructType([
		StructField("street", StringType()),
		StructField("city", StringType()),
		StructField("zip", IntegerType())
	]))
])

# Create the DataFrame
data = [("Alice", 25, {"street": "Main St", "city": "Anytown", "zip": 12345}),
		("Bob", 30, {"street": "Park Ave", "city": "New York", "zip": 56789})]
df = spark.createDataFrame(data, schema)

# Show the DataFrame
df.show()
#print the Schema
df.printSchema()
