# Importing required modules
from pyspark.sql.types import StructType, StructField, StringType, IntegerType
from pyspark.sql import SparkSession

# Create a SparkSession
spark = SparkSession.builder.appName("Metadata").getOrCreate()

# Define schema of data frame
schema = StructType([
	StructField("name", StringType()),
	StructField("age", IntegerType())
])

# Create data frame
data = [("Alice", 25),
		("Bob", 30),
		("Charlie", 35)]
df = spark.createDataFrame(data, schema)

# Access and view the metadata
print(df.schema)
df.printSchema()
