# Importing required modules
from pyspark.sql.types import StructType, StructField, StringType, IntegerType
from pyspark.sql import SparkSession

# Create a SparkSession
spark = SparkSession.builder.appName("Metadata").getOrCreate()

# Create a DataFrame
schema = StructType([
	StructField("name", StringType()),
	StructField("age", IntegerType())
])
# Create a DataFrame
data = [("Alice", 25),
		("Bob", 30),
		("Charlie", 35)]
df = spark.createDataFrame(data,
						["name", "age"])
# print schema of data frame
df.printSchema()

# Change column names
df = df.withColumnRenamed("name", "username")
df.printSchema()
